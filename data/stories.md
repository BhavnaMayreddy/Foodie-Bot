## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - verify_cuisines
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - verify_location
    - slot{"location": "Chennai"}
    - slot{"loc_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
* affirm
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "dubai"}
    - slot{"location": "dubai"}
    - verify_location
    - slot{"location": null}
    - slot{"loc_verified": false}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - verify_cuisines
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - verify_location
    - slot{"location": "Lucknow"}
    - slot{"loc_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"resto_inbudget": false}
    - utter_recheck_budget
* affirm
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* send_mail{"email": "mereddy248@gmail.com"}
    - slot{"email": "mereddy248@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "mereddy248@gmail.com"}
    - action_send_mail
    - slot{"email": "mereddy248@gmail.com"}
    - slot{"email_sent": true}
* affirm

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - verify_location
    - slot{"location": "New Delhi"}
    - slot{"loc_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - verify_cuisines
    - slot{"cuisine": null}
    - slot{"cuisine_verified": false}
    - utter_reask_forcuisines
* affirm
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - verify_cuisines
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* dont_send_mail
    - utter_thanks
* thankyou

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Goa", "budget": "mid"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Goa"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Goa"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"restaurant_existence": false}
    - utter_reask_forcuisines
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - verify_cuisines
    - slot{"cuisine": "Italian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"resto_inbudget": false}
    - utter_recheck_budget
* affirm
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
* thankyou
    - utter_thanks
    
## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "goa"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "goa"}
    - verify_location
    - slot{"location": "Goa"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"restaurant_existence": false}
    - utter_reask_forcuisines
* affirm
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"restaurant_existence": false}
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - verify_cuisines
    - slot{"cuisine": "Italian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"resto_inbudget": false}
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
* thankyou
    - utter_thanks

## Complete input by user with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "noida", "budget": "mid"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "noida"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Noida"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* send_mail
    - utter_ask_emailid
* send_mail{"email": "mereddy248@gmail.com"}
    - slot{"email": "mereddy248@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "mereddy248@gmail.com"}
    - action_send_mail
    - slot{"email": "mereddy248@gmail.com"}
    - slot{"email_sent": true}
* thankyou
    - utter_thanks

## User input with just location,recheck budget and later send email with details
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - verify_location
    - slot{"location": "Jaipur"}
    - slot{"loc_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - slot{"resto_inbudget": false}
    - utter_recheck_budget
* affirm
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* send_mail
    - utter_ask_emailid
* send_mail{"email": "mereddy248@gmail.com"}
    - slot{"email": "mereddy248@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - action_send_mail
    - slot{"email": "mereddy248@gmail.com"}
    - slot{"email_sent": true}
    - utter_goodbye
* Thanks
    - utter_goodbye

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Jaipur", "budget": "High"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Jaipur"}
    - slot{"budget": "High"}
    - verify_location
    - slot{"location": "Jaipur"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
* affirm
    - utter_ask_moreinfo
* send_mail
    - utter_ask_emailid
* send_mail{"email": "mereddy248@gmail.com"}
    - slot{"email": "mereddy248@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "mereddy248@gmail.com"}
    - action_send_mail
    - slot{"email": "mereddy248@gmail.com"}
    - slot{"email_sent": true}
    - utter_goodbye
* affirm
    - utter_thanks

## interactive_story_ask location,cuisine,budget and sent email
* greet{"text": "hola"}
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Allahabad"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* send_mail
    - utter_ask_emailid
* send_mail{"email": "vnk2611@gmail.com"}
    - slot{"email": "vnk2611@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "vnk2611@gmail.com"}
    - action_send_mail
    - slot{"email": "vnk2611@gmail.com"}
    - slot{"email_sent": true}

## Use choose unoperating location, recheck location without email
* greet
    - utter_greet
* restaurant_search{"location": "Shadnagar"}
    - slot{"location": "Shadnagar"}
    - verify_location
    - slot{"location": null}
    - slot{"loc_verified": false}
* restaurant_search{"location": "secunderabd"}
    - slot{"location": "secunderabd"}
    - verify_location
    - slot{"location": "Secunderabad"}
    - slot{"loc_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Secunderabad"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* dont_send_mail
    - utter_thanks

## user with location,cuisine, ask budget and email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Allahabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Allahabad"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Allahabad"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* affirm
    - utter_ask_emailid
* send_mail{"email": "mayreddy.bhavana@gmail.com"}
    - slot{"email": "mayreddy.bhavana@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "mayreddy.bhavana@gmail.com"}
    - action_send_mail
    - slot{"email": "mayreddy.bhavana@gmail.com"}
    - slot{"email_sent": true}
    - utter_goodbye

## Search over various budget ranges
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - verify_location
    - slot{"location": "Patna"}
    - slot{"loc_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - verify_cuisines
    - slot{"cuisine": null}
    - slot{"cuisine_verified": false}
    - utter_reask_forcuisines
* affirm
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "Low"}
    - slot{"budget": "Low"}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"resto_inbudget": false}
    - utter_recheck_budget
* affirm
    - utter_ask_budget
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"resto_inbudget": false}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"resto_inbudget": false}
    - utter_recheck_budget
* affirm
    - utter_ask_budget
* greet
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* affirm
    - utter_ask_emailid
* send_mail{"email": "nani.doux.souvenirs@gmail.com"}
    - slot{"email": "nani.doux.souvenirs@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "nani.doux.souvenirs@gmail.com"}
    - action_send_mail
    - slot{"email": "nani.doux.souvenirs@gmail.com"}
    - slot{"email_sent": true}
    - utter_goodbye

## cuisine,budget with location choosen
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "budget": "mid"}
    - slot{"cuisine": "South Indian"}
    - slot{"budget": "mid"}
    - utter_ask_location
* restaurant_search{"location": "Gurugaon"}
    - slot{"location": "Gurugaon"}
    - verify_location
    - slot{"location": "Gurgaon"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Gurgaon"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* affirm
    - utter_ask_emailid
* send_mail{"email": "mereddy248@gmail.com"}
    - slot{"email": "mereddy248@gmail.com"}
    - action_validate_email
    - slot{"email_verified": true}
    - slot{"email": "mereddy248@gmail.com"}
    - action_send_mail
    - slot{"email": "mereddy248@gmail.com"}
    - slot{"email_sent": true}
    - utter_goodbye

## Cuisine searched with choosen location and budget range
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisines
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "bubaneshwar"}
    - slot{"location": "bubaneshwar"}
    - verify_location
    - slot{"location": "Bhubaneshwar"}
    - slot{"loc_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Bhubaneshwar"}
    - slot{"loc_verified": true}
    - action_search_restaurants
    - slot{"location": "Bhubaneshwar"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* dont_send_mail
    - utter_thanks

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"budget": "High", "cuisine": "South Indian", "location": "Srinagar"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Srinagar"}
    - slot{"budget": "High"}
    - verify_location
    - slot{"location": null}
    - slot{"loc_verified": false}
* thankyou
    - utter_thanks

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"budget": "mid", "cuisine": "mexican", "location": "noida"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "noida"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Noida"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* dont_send_mail
    - utter_goodbye

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "hyderabad", "budget": "mid"}
    - slot{"cuisine": "american"}
    - slot{"location": "hyderabad"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "Hyderabad"}
    - slot{"loc_verified": true}
    - verify_cuisines
    - slot{"cuisine": "american"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"resto_inbudget": false}
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
* dont_send_mail
    - utter_thanks

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"budget": "High"}
    - slot{"budget": "High"}
    - utter_ask_location
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - verify_location
    - slot{"location": "Surat"}
    - slot{"loc_verified": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - slot{"resto_inbudget": false}
    - utter_recheck_budget
* affirm
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - slot{"restaurant_existence": true}
    - slot{"resto_inbudget": true}
    - utter_ask_moreinfo
* affirm
    - utter_ask_emailid
* send_mail{"email": "123-5689@today@gmail.com"}
    - slot{"email": "123-5689@today@gmail.com"}
    - action_validate_email
    - slot{"email": null}
    - slot{"email_verified": false}
* dont_send_mail
    - utter_thanks
* affirm
    - utter_goodbye

## interactive_story_15
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "muxmai"}
    - slot{"location": "muxmai"}
    - verify_location
    - slot{"location": null}
    - slot{"loc_verified": false}
* unknown text
    - utter_default
* thankyou
    - utter_thanks