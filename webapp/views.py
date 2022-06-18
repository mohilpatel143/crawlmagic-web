from django.shortcuts import render
from .models import Subscrib, Contact
from django.core.mail import send_mail
from django.conf import settings

# for sendig mail
# from django.core.mail import EmailMultiAlteratives
# from django.core.mail import EmailMultiAlteratives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

from django.template.loader import get_template
from django.core.mail import EmailMessage


# Create your views here.


# ========================== Main Header ==========================
def home(request):
    if request.method=="POST":
        email = request.POST.get('email', '')
        subscrib = Subscrib(email=email)
        subscrib.save()
        
        html_tpl_path = 'webapp/email-message.html'
        context_data = {'email': f"{email}" }
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = 'patelmohil143@gmail.com'
        email_msg = EmailMessage('Welcome from django app', 
                                    email_html_template, 
                                    settings. APPLICATION_EMAIL,
                                    [receiver_email],
                                    reply_to=[settings.APPLICATION_EMAIL]
                                    )
        # this is the crucial part that sends email as html content but not as a plain text
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)





    # to = request.POST.get('patelmohil143@gmail.com')
    # content = request.POST.get('content')

    # html_content = render_to_string("webapp/email-message.html", {'title':'test email', 'content':content})
    # test_content = strip_tags(html_content)
    
    # email = send_mail(
    #     "testing",
    #     test_content,
    #     settings.EMAIL_HOST_USER,
    #     [to]
    # )
    # email.attach_alternative(html_content, 'text/html')
    # email.send(fail_silently=False)




    # if request.method=="POST":
    #     email = request.POST.get('email', '')
    #     subscrib = Subscrib(email=email)
    #     subscrib.save()

    #     send_mail('Welcome user',                      # subject
    #     f"{email} Came in Contact With Our Site.",     # message
    #     'mohil.crawlmagic@gmail.com',                  # from
    #     ['patelmohil143@gmail.com'],                   # to
    #     fail_silently=False)
    return render(request, 'webapp/index.html')


def services(request):
    return render(request, 'webapp/services.html')

def pricing(request):
    return render(request, "webapp/pricing.html")

def itsolution(request):
    return render(request, 'webapp/index-9.html')

def aboutus(request):
    return render(request, 'webapp/about-us.html')

def contactus(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(first_name=first_name, last_name=last_name, phone=phone, email=email, message=message)
        contact.save()
 

        html_tpl_path = 'webapp/contact-us-message.html'
        context_data =  {'firstname': f"{first_name}", 'lastname': f"{last_name}", 'phone': f"{phone}", 'email': f"{email}", 'message': f"{message}" }
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = 'patelmohil143@gmail.com'
        email_msg = EmailMessage('Welcome from django app', 
                                    email_html_template, 
                                    settings. APPLICATION_EMAIL,
                                    [receiver_email],
                                    reply_to=[settings.APPLICATION_EMAIL]
                                    )
        # this is the crucial part that sends email as html content but not as a plain text
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)


        # send_mail('Contact Details',
        #           f"{first_name} {last_name}'s Data Received",
        #           'mohil.crawlmagic@gmail.com',               
        #           ['patelmohil143@gmail.com'], 
        #           fail_silently=False)
    return render(request, 'webapp/contact-us.html')

def career(request):
    return render(request, 'webapp/career.html')

def support(request):
    return render(request, 'webapp/support.html')

def notfound(request):
    return render(request, 'webapp/404.html')


# ========================== Services / Web_Scraping_Services ==========================
def enterprise_web_crawling(request):
    return render(request, 'webapp/services/web_scraping_services/enterprise_web_crawling.html')

def mobile_app_scraping(request):
    return render(request, 'webapp/services/web_scraping_services/mobile_app_scraping.html')

def web_scraping_API(request):
    return render(request, 'webapp/services/web_scraping_services/web_scraping_API.html')    

def hosted_web_crawling_services(request):
    return render(request, 'webapp/services/web_scraping_services/hosted_web_crawling_services.html')    


# ========================== Services / Advanced Scraping Services ==========================
def python_scrapy_consulting(request):
    return render(request, 'webapp/services/advanced_scraping_services/python_scrapy_consulting.html')

def robotic_process_automation(request):
    return render(request, 'webapp/services/advanced_scraping_services/robotic_process_automation.html')    

def dark_and_deep_web_data_scraping(request):
    return render(request, 'webapp/services/advanced_scraping_services/dark_and_deep_web_data_scraping.html')    


# ========================== Services / Data Enrichment ==========================
def data_appending(request):
    return render(request, 'webapp/services/data_enrichment/data_appending.html')

def image_OCR_services(request):
    return render(request, 'webapp/services/data_enrichment/image_OCR_services.html')  

def data_entry_and_data_processing(request):
    return render(request, 'webapp/services/data_enrichment/data_entry_and_data_processing.html')      



# ========================== Services / AI & Data Analytics ==========================
def machine_learning(request):
    return render(request, 'webapp/services/AI_and_data_analytics/machine_learning.html')

def sentiment_analysis(request):
    return render(request, 'webapp/services/AI_and_data_analytics/sentiment_analysis.html')    

def data_visualization(request):
    return render(request, 'webapp/services/AI_and_data_analytics/data_visualization.html')    





# ========================== Idustries / E-commerce ==========================
def retail_pricing_intelligence(request):
    return render(request, 'webapp/industries/e-commerce/retail_pricing_intelligence.html')

def price_monitoring(request):
    return render(request, 'webapp/industries/e-commerce/price_monitoring.html')    

def pricing_intelligence(request):
    return render(request, 'webapp/industries/e-commerce/pricing_intelligence.html')    

def channel_pricing_intelligence(request):
    return render(request, 'webapp/industries/e-commerce/channel_pricing_intelligence.html')    

def tyre_pricing_intelligence(request):
    return render(request, 'webapp/industries/e-commerce/tyre_pricing_intelligence.html')

def brand_monitoring(request):
    return render(request, 'webapp/industries/e-commerce/brand_monitoring.html')    

def product_pricing_and_review_data_scraping(request):
    return render(request, 'webapp/industries/e-commerce/product_pricing_and_review_data_scraping.html')    

def amazon_data_scraping(request):
    return render(request, 'webapp/industries/e-commerce/amazon_data_scraping.html')   

def ecommerce_pricing_intelligence(request):
    return render(request, 'webapp/industries/e-commerce/ecommerce_pricing_intelligence.html')     

def lazada_data_scraping_services(request):
    return render(request, 'webapp/industries/e-commerce/lazada_data_scraping_services.html')

def shopee_data_scraping_service(request):
    return render(request, 'webapp/industries/e-commerce/shopee_data_scraping_service.html')    



# ========================== Idustries / Travel ========================== 
def flight_pricing_intelligence(request):
    return render(request, 'webapp/industries/travel/flight_pricing_intelligence.html')

def travel_data_intelligence(request):
    return render(request, 'webapp/industries/travel/travel_data_intelligence.html')  

def vacation_rental_intelligence(request):
    return render(request, 'webapp/industries/travel/vacation_rental_intelligence.html')      

def hotel_pricing_intelligence(request):
    return render(request, 'webapp/industries/travel/hotel_pricing_intelligence.html')    


# ========================== Idustries / Food Delivery ========================== 
def competitor_pricing_for_food_delivery(request):
    return render(request, 'webapp/industries/food_delivery/competitor_pricing_for_food_delivery.html')

def food_delivery_aggregator(request):
    return render(request, 'webapp/industries/food_delivery/food_delivery_aggregator.html')   

def grocery_delivery_app_scraping_services(request):
    return render(request, 'webapp/industries/food_delivery/grocery_delivery_app_scraping_services.html')     

def online_food_ordering_app_scraping(request):
    return render(request, 'webapp/industries/food_delivery/online_food_ordering_app_scraping.html')    

def nutrition_facts_food_data_scraping_services(request):
    return render(request, 'webapp/industries/food_delivery/nutrition_facts_food_data_scraping_services.html')    

def restaurant_data_scraping(request):
    return render(request, 'webapp/industries/food_delivery/restaurant_data_scraping.html')   

def uber_eats_data_scraping_services(request):
    return render(request, 'webapp/industries/food_delivery/uber_eats_data_scraping_services.html')     

def zomato_restaurant_data_scraping(request):
    return render(request, 'webapp/industries/food_delivery/zomato_restaurant_data_scraping.html')    


# ========================== Idustries / Social Media ==========================     
def facebook_data_scraping(request):
    return render(request, 'webapp/industries/social_media/facebook_data_scraping.html')

def instagram_data_scraping(request):
    return render(request, 'webapp/industries/social_media/instagram_data_scraping.html')    

def linkedIn_data_scraping(request):
    return render(request, 'webapp/industries/social_media/linkedIn_data_scraping.html')    

def quora_data_scraping(request):
    return render(request, 'webapp/industries/social_media/quora_data_scraping.html')    

def tikTok_data_scraping(request):
    return render(request, 'webapp/industries/social_media/tikTok_data_scraping.html')    

def twitter_data_scraping(request):
    return render(request, 'webapp/industries/social_media/twitter_data_scraping.html') 

def youTube_data_scraping(request):
    return render(request, 'webapp/industries/social_media/youTube_data_scraping.html')      

def social_media_monitoring(request):
    return render(request, 'webapp/industries/social_media/social_media_monitoring.html')     


# ========================== Idustries / Entertainment ==========================  

def streaming_OTT_platform_app_data(request):
    return render(request, 'webapp/industries/entertainment/streaming_OTT_platform_app_data.html')

def movie_showtime_intelligence(request):
    return render(request, 'webapp/industries/entertainment/movie_showtime_intelligence.html')

def netflix_data_scraping(request):
    return render(request, 'webapp/industries/entertainment/netflix_data_scraping.html')    


# ========================== Idustries / Real Estate ==========================     
def real_estate_data_intelligence(request):
    return render(request, 'webapp/industries/real_estate/real_estate_data_intelligence.html')


# ========================== Idustries / Recruitment ========================== 
def job_listings_and_data_feeds(request):
    return render(request, 'webapp/industries/recruitment/job_listings_and_data_feeds.html')

def human_capital_management(request):
    return render(request, 'webapp/industries/recruitment/human_capital_management.html')


# ========================== Idustries / News & Media ==========================    
def news_aggregation_and_intelligence(request):
    return render(request, 'webapp/industries/news_and_media/news_aggregation_and_intelligence.html')

def data_for_research_and_journalism_scraping(request):
    return render(request, 'webapp/industries/news_and_media/data_for_research_and_journalism_scraping.html')    


# ========================== Idustries / Finance ==========================  
def stock_market_and_financial_data_scraping(request):
    return render(request, 'webapp/industries/finance/stock_market_and_financial_data_scraping.html')  

def alternative_data(request):
    return render(request, 'webapp/industries/finance/alternative_data.html')    

# ========================== Idustries / Data Aggregation ==========================    
def data_intelligence(request):
    return render(request, 'webapp/industries/data_aggregation/data_intelligence.html')

def location_intelligence(request):
    return render(request, 'webapp/industries/data_aggregation/location_intelligence.html')    

def customer_intelligence(request):
    return render(request, 'webapp/industries/data_aggregation/customer_intelligence.html')

def sales_intelligence(request):
    return render(request, 'webapp/industries/data_aggregation/sales_intelligence.html')        
