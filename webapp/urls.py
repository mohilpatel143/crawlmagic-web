from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("services/", views.services, name="services"),
    path("pricing/", views.pricing, name="pricing"),
    path("itsolution/", views.itsolution, name="itsolution"),
    path("about-us/", views.aboutus, name="about-us"),
    path("contact-us/", views.contactus, name="contact-us"),
    path("career/", views.career, name="career"),
    path("support/", views.support, name="support"),
    path("404/", views.notfound, name="404"),


    # ======================= Services / Web_Scraping_Services =======================
    path("enterprise_web_crawling/", views.enterprise_web_crawling, name="enterprise_web_crawling"),
    path("mobile_app_scraping/", views.mobile_app_scraping, name="mobile_app_scraping"),
    path("web_scraping_API/", views.web_scraping_API, name="web_scraping_API"),
    path("hosted_web_crawling_services/", views.hosted_web_crawling_services, name="hosted_web_crawling_services"),

    # ======================= Services / Advanced Scraping Services =======================
    path("python_scrapy_consulting/", views.python_scrapy_consulting, name="python_scrapy_consulting"),
    path("robotic_process_automation/", views.robotic_process_automation, name="robotic_process_automation"),
    path("dark_and_deep_web_data_scraping/", views.dark_and_deep_web_data_scraping, name="dark_and_deep_web_data_scraping"),


    # ======================= Services / Data Enrichment =======================
    path("data_appending/",views.data_appending, name="data_appending"),
    path("image_OCR_services/", views.image_OCR_services, name="image_OCR_services"),
    path("data_entry_and_data_processing/", views.data_entry_and_data_processing, name="data_entry_and_data_processing"),


    # ======================= Services / AI & Data Analytics =======================
    path("machine_learning/", views.machine_learning, name="machine_learning"),
    path("sentiment_analysis/", views.sentiment_analysis, name="sentiment_analysis"),
    path("data_visualization/", views.data_visualization, name="data_visualization"),


    # ======================= Industries/E-commerce ======================= 
    path("retail_pricing_intelligence/", views.retail_pricing_intelligence, name="retail_pricing_intelligence"),
    path("price_monitoring/", views.price_monitoring, name="price_monitoring"),
    path("pricing_intelligence/", views.pricing_intelligence, name="pricing_intelligence"),
    path("channel_pricing_intelligence/", views.channel_pricing_intelligence, name="channel_pricing_intelligence"),
    path("tyre_pricing_intelligence/", views.tyre_pricing_intelligence, name="tyre_pricing_intelligence"),
    path("brand_monitoring/", views.brand_monitoring, name="brand_monitoring"),
    path("product_pricing_and_review_data_scraping/", views.product_pricing_and_review_data_scraping, name="product_pricing_and_review_data_scraping"),
    path("amazon_data_scraping/", views.amazon_data_scraping, name="amazon_data_scraping"),
    path("ecommerce_pricing_intelligence/", views.ecommerce_pricing_intelligence, name="ecommerce_pricing_intelligence"),
    path("lazada_data_scraping_services/", views.lazada_data_scraping_services, name="lazada_data_scraping_services"),
    path("shopee_data_scraping_service/", views.shopee_data_scraping_service, name="shopee_data_scraping_service"),

    # ======================= Travel ======================= 
    path("flight_pricing_intelligence/", views.flight_pricing_intelligence, name="flight_pricing_intelligence"),
    path("travel_data_intelligence/", views.travel_data_intelligence, name="travel_data_intelligence"),
    path("vacation_rental_intelligence/", views.vacation_rental_intelligence, name="vacation_rental_intelligence"),
    path("hotel_pricing_intelligence/", views.hotel_pricing_intelligence, name="hotel_pricing_intelligence"),

    # ======================= Food Delivery ======================= 
    path("competitor_pricing_for_food_delivery/", views.competitor_pricing_for_food_delivery, name="competitor_pricing_for_food_delivery"),
    path("food_delivery_aggregator/", views.food_delivery_aggregator, name="food_delivery_aggregator"),
    path("grocery_delivery_app_scraping_services/", views.grocery_delivery_app_scraping_services, name="grocery_delivery_app_scraping_services"),
    path("online_food_ordering_app_scraping/", views.online_food_ordering_app_scraping, name="online_food_ordering_app_scraping"),
    path("nutrition_facts_food_data_scraping_services/", views.nutrition_facts_food_data_scraping_services, name="nutrition_facts_food_data_scraping_services"),
    path("restaurant_data_scraping/", views.restaurant_data_scraping, name="restaurant_data_scraping"),
    path("uber_eats_data_scraping_services/", views.uber_eats_data_scraping_services, name="uber_eats_data_scraping_services"),
    path("zomato_restaurant_data_scraping/", views.zomato_restaurant_data_scraping, name="zomato_restaurant_data_scraping"),

    # ======================= Social Media ======================= 
    path("facebook_data_scraping/", views.facebook_data_scraping, name="facebook_data_scraping"),
    path("instagram_data_scraping/", views.instagram_data_scraping, name="instagram_data_scraping"),
    path("linkedIn_data_scraping/", views.linkedIn_data_scraping, name="linkedIn_data_scraping"),
    path("quora_data_scraping/", views.quora_data_scraping, name="quora_data_scraping"),
    path("tikTok_data_scraping/", views.tikTok_data_scraping, name="tikTok_data_scraping"),
    path("twitter_data_scraping/", views.twitter_data_scraping, name="twitter_data_scraping"),
    path("youTube_data_scraping/", views.youTube_data_scraping, name="youTube_data_scraping"),
    path("social_media_monitoring/", views.social_media_monitoring, name="social_media_monitoring"),

    # ======================= Entertainment ======================= 
    path("streaming_OTT_platform_app_data/", views.streaming_OTT_platform_app_data, name="streaming_OTT_platform_app_data"),
    path("movie_showtime_intelligence/", views.movie_showtime_intelligence, name="movie_showtime_intelligence"),
    path("netflix_data_scraping/", views.netflix_data_scraping, name="netflix_data_scraping"),

    # ======================= Real Estate ======================= 
    path("real_estate_data_intelligence/", views.real_estate_data_intelligence, name="real_estate_data_intelligence"),

    # ========================== Recruitment ==========================  
    path("job_listings_and_data_feeds/", views.job_listings_and_data_feeds, name="job_listings_and_data_feeds"),
    path("human_capital_management/", views.human_capital_management, name="human_capital_management"),

    # ========================== News & Media ==========================
    path("news_aggregation_and_intelligence/", views.news_aggregation_and_intelligence, name="news_aggregation_and_intelligence"),
    path("data_for_research_and_journalism_scraping/", views.data_for_research_and_journalism_scraping, name="data_for_research_and_journalism_scraping"),

    # ========================== Finance ==========================  
    path("stock_market_and_financial_data_scraping/", views.stock_market_and_financial_data_scraping, name="stock_market_and_financial_data_scraping"),
    path("alternative_data/", views.alternative_data, name="alternative_data"),

    # ========================== Data Aggregation ==========================  
    path("data_intelligence/", views.data_intelligence, name="data_intelligence"),
    path("location_intelligence/", views.location_intelligence, name="location_intelligence"),
    path("customer_intelligence/", views.customer_intelligence, name="customer_intelligence"),
    path("sales_intelligence/", views.sales_intelligence, name="sales_intelligence"),
]