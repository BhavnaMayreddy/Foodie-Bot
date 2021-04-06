from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import re
from prompt_toolkit import print_formatted_text, HTML
import json

from spellcorrection_loc import get_soundex_location,spellcheck
from email_trigger import sendmail

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
#WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
WeOperate = ['Agra', 'Ahmedabad', 'Allahabad', 'Amritsar', 'Aurangabad', 'Bangalore', 'Bhopal', 'Bhubaneshwar', 'Chandigarh', 'Chennai', 'Coimbatore', 'Dehradun', 'Faridabad', 'Gangtok', 'Ghaziabad', 'Goa', 'Gurgaon', 'Guwahati', 'Hyderabad', 'Indore', 'Jaipur', 'Kanpur', 'Kochi', 'Kolkata', 'Lucknow', 'Ludhiana', 'Mangalore', 'Mohali', 'Mumbai', 'Mysore', 'Nagpur', 'Nashik', 'New Delhi', 'Noida', 'Ooty', 'Panchkula', 'Patna', 'Puducherry', 'Pune', 'Ranchi', 'Secunderabad', 'Shimla', 'Surat', 'Vadodara', 'Varanasi', 'Vizag']
Cuisines_list = ['Italian','Mexican','American','North Indian','South Indian','Chinese']
prices_dict =  {'low':{'min':0,'max':300},'mid':{'min':300,'max':700},'high':{'min':700,'max':10000}}

def restaurant_cuisine_search(city,cuisine):
    rest_df = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x:cuisine.lower() in x.lower())) &  (ZomatoData['City'].apply(lambda x: city.lower() in x.lower()))].sort_values(by='Aggregate rating',ascending=False)[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]
    return rest_df

def restaurant_inbudget(budgetrange,rest_df):
    df_resto = rest_df[(rest_df['Average Cost for two'] >= prices_dict[budgetrange]['min']) & (rest_df['Average Cost for two'] < prices_dict[budgetrange]['max'])]
    return df_resto

class VerifyLocation(Action):
    def name(self):
        return "verify_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        loccode_list = get_soundex_location(WeOperate)
        loc_requested = spellcheck(loc,loccode_list)
        if(loc_requested in WeOperate):
            #dispatcher.utter_template("utter_other_cities", tracker)
            #loc = tracker.get_slot('location')
            #loc_verified = True
            return [SlotSet('location', loc_requested), SlotSet("loc_verified", True)]
        else:
            #loc_verified = False
            dispatcher.utter_message("Sorry, we dont operate in "+ loc_requested +" yet. Please try other city")
            return [SlotSet('location',None),SlotSet("loc_verified",False)]
        #if(loc_verified ==False):
            #dispatcher.utter_message("Sorry, we dont operate in "+ loc +" yet. Please try other city")
            #return [Slotset('location',None),Slotset("loc_verified",loc_verified)]
        #else:
            #return [Slotset('location',loc),Slotset("loc_verified",loc_verified)]


    #def verify_location(self, loc):
        #return loc.lower()

class VerifyCuisines(Action):
    def name(self):
        return "verify_cuisines"

    def run(self,dispatcher,tracker,domain):
        cuisine = tracker.get_slot('cuisine')
        if(cuisine.title() in Cuisines_list):
            cuisine = tracker.get_slot('cuisine')
            return [SlotSet('cuisine', cuisine), SlotSet("cuisine_verified", True)]
        else:
            dispatcher.utter_message("Sorry, we dont serve this cuisines. Please try some other cuisines")
            return [SlotSet('cuisine',None),SlotSet('cuisine_verified',False)]

        if(self.verify_cuisines(cuisine)== False):
            dispatcher.utter_template("utter_reask_forcuisines",tracker)
            dispatcher.utter_message("Sorry, we dont serve this cuisines. Please try some others")
            return [SlotSet('cuisine', None), SlotSet("cuisine_verified", False)]
        else:
            return [SlotSet('cuisine', cuisine), SlotSet("cuisine_verified", True)]

    #def verify_cuisines(self,cuisine):
        #return cuisine.lower()
    
class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        email_check = tracker.get_slot('email')
        if email_check is not None:
            if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_check):
                return [SlotSet('email_verified', True), SlotSet('email', email_check)]
            else:
                dispatcher.utter_message("Sorry this is not a valid email. please check for typing errors")
                return [SlotSet('email', None),SlotSet("email_verified", False)]
        else:
            dispatcher.utter_message("Sorry I could'nt understand the email address you provided? Please provide again")
            return [SlotSet('email', None)]

class ActionSlotReset(Action): 
    def name(self): 
        return 'action_slot_reset' 
    def run(self, dispatcher, tracker, domain): 
        return[AllSlotsReset()]

class ActionRestarted(Action):
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
    
    def run(self,dispatcher,tracker,domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budgetrange = tracker.get_slot('budget')
        #initialize strings
        res = ''
        response = 'List of Restaurants:\n'
        global restaurants_results
        global restaurants_results_email
        #get list of reataurants for cuisine and location
        df_resto = restaurant_cuisine_search(loc,cuisine)
        if (len(df_resto)>0):
            SlotSet("restaurant_existence",True)
            #[Slotset('location',loc),Slotset("restaurant_existence",True)]
            # get restaurants in price range
            pricerange = budgetrange.lower()
            df_results = restaurant_inbudget(pricerange,df_resto)
            if(len(df_results) > 0):
                SlotSet("resto_inbudget", True)
                df_5 = df_results.head(5)
                #[SlotSet('location', loc), SlotSet("resto_inbudget", True)]
                for index,row in df_5.iterrows():
                    res= res + "Found : {0} in {1} has been rated {2} with avg cost per 2 persons as {3} \n".format(row['Restaurant Name'],row['Address'],row['Aggregate rating'],row['Average Cost for two'])
                    restaurants_results = response+'\n'+res
                print(restaurants_results)
                df_10 = df_results.head(10)
                res1=''
                for index,row in df_10.iterrows():
                    #res1= res1 + "Found : <strong>{0}</strong> in <em>{1}</em> has been rated <strong>{2}</strong> with avg cost per 2 persons as <strong>{3}</strong> \n".format(row['Restaurant Name'],row['Address'],row['Aggregate rating'],row['Average Cost for two'])
                    res= res + "Found : {0} in {1} has been rated {2} with avg cost per 2 persons as {3} \n".format(row['Restaurant Name'],row['Address'],row['Aggregate rating'],row['Average Cost for two'])
                    restaurants_results_email = response+'\n'+res
                #print(response+'\n'+res1)
            else:
                print('No restaurants in the choosen pricerange.')
                dispatcher.utter_message("-----"+'No restaurants in the choosen pricerange.')
                dispatcher.utter_template('utter_no_resto_inbudget',tracker)
        #return 'utter_no_restaurants'
                return [SlotSet('location', loc), SlotSet("resto_inbudget", False)]
        else:
            print('No restaurants available with the location and cuisine')
            dispatcher.utter_message("-----"+'No restaurants available with the location and cuisine')
            #dispatcher.utter_template('utter_no_restaurants',tracker)
            dispatcher.utter_message(template='utter_no_restaurants')
            #return 'utter_no_restaurants'
            return [SlotSet('location', loc), SlotSet("restaurant_existence", False)]
        dispatcher.utter_message("-----"+restaurants_results)
        #SlotSet("restaurant_existence",True)
        #SlotSet("resto_inbudget", True)
        return [SlotSet('location',loc),SlotSet("restaurant_existence",True),SlotSet("resto_inbudget", True)]

class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        MailID = tracker.get_slot('email')
        print(MailID)
        print(restaurants_results_email)
        try:
            if(MailID):
                print(restaurants_results_email)
                sendmail(MailID,restaurants_results_email)
                dispatcher.utter_message("Have a great day! Mail is sent")
                return [SlotSet('email',MailID),SlotSet('email_sent',True)]
            else:
                dispatcher.utter_message("Email not sent, address is not valid")
                return [SlotSet('email',None),SlotSet('email_sent',False)]
        except:
            dispatcher.utter_message("Email not sent, address is not valid")
            return [SlotSet('email',None),SlotSet('email_sent',False)]
