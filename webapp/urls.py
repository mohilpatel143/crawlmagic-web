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
    path("enterprise-web-crawling/", views.enterprise_web_crawling, name="enterprise-web-crawling"),
    path("mobile-app-scraping/", views.mobile_app_scraping, name="mobile_app_scraping"),
    path("web-scraping-API/", views.web_scraping_API, name="web_scraping_API"),
    path("hosted-web-crawling-services/", views.hosted_web_crawling_services, name="hosted_web_crawling_services"),

    # ======================= Services / Advanced Scraping Services =======================
    path("python-scrapy-consulting/", views.python_scrapy_consulting, name="python_scrapy_consulting"),
    path("robotic-process-automation/", views.robotic_process_automation, name="robotic_process_automation"),
    path("dark-and-deep-web-data-scraping/", views.dark_and_deep_web_data_scraping, name="dark_and_deep_web_data_scraping"),


    # ======================= Services / Data Enrichment =======================
    path("data-appending/",views.data_appending, name="data_appending"),
    path("image-OCR-services/", views.image_OCR_services, name="image_OCR_services"),
    path("data-entry-and-data-processing/", views.data_entry_and_data_processing, name="data_entry_and_data_processing"),


    # ======================= Services / AI & Data Analytics =======================
    path("machine-learning/", views.machine_learning, name="machine_learning"),
    path("sentiment-analysis/", views.sentiment_analysis, name="sentiment_analysis"),
    path("data-visualization/", views.data_visualization, name="data_visualization"),


    # ======================= Industries/E-commerce ======================= 
    path("retail-pricing-intelligence/", views.retail_pricing_intelligence, name="retail_pricing_intelligence"),
    path("price-monitoring/", views.price_monitoring, name="price_monitoring"),
    path("pricing-intelligence/", views.pricing_intelligence, name="pricing_intelligence"),
    path("channel-pricing-intelligence/", views.channel_pricing_intelligence, name="channel_pricing_intelligence"),
    path("tyre-pricing-intelligence/", views.tyre_pricing_intelligence, name="tyre_pricing_intelligence"),
    path("brand-monitoring/", views.brand_monitoring, name="brand_monitoring"),
    path("product-pricing-and-review-data-scraping/", views.product_pricing_and_review_data_scraping, name="product_pricing_and_review_data_scraping"),
    path("amazon-data-scraping/", views.amazon_data_scraping, name="amazon_data_scraping"),
    path("ecommerce-pricing-intelligence/", views.ecommerce_pricing_intelligence, name="ecommerce_pricing_intelligence"),
    path("lazada-data-scraping-services/", views.lazada_data_scraping_services, name="lazada_data_scraping_services"),
    path("shopee-data-scraping-service/", views.shopee_data_scraping_service, name="shopee_data_scraping_service"),

    # ======================= Travel ======================= 
    path("flight-pricing-intelligence/", views.flight_pricing_intelligence, name="flight_pricing_intelligence"),
    path("travel-data-intelligence/", views.travel_data_intelligence, name="travel_data_intelligence"),
    path("vacation-rental-intelligence/", views.vacation_rental_intelligence, name="vacation_rental_intelligence"),
    path("hotel-pricing-intelligence/", views.hotel_pricing_intelligence, name="hotel_pricing_intelligence"),

    # ======================= Food Delivery ======================= 
    path("competitor-pricing-for-food-delivery/", views.competitor_pricing_for_food_delivery, name="competitor_pricing_for_food_delivery"),
    path("food-delivery-aggregator/", views.food_delivery_aggregator, name="food_delivery_aggregator"),
    path("grocery-delivery-app-scraping-services/", views.grocery_delivery_app_scraping_services, name="grocery_delivery_app_scraping_services"),
    path("online-food-ordering-app-scraping/", views.online_food_ordering_app_scraping, name="online_food_ordering_app_scraping"),
    path("nutrition-facts-food-data-scraping-services/", views.nutrition_facts_food_data_scraping_services, name="nutrition_facts_food_data_scraping_services"),
    path("restaurant-data-scraping/", views.restaurant_data_scraping, name="restaurant_data_scraping"),
    path("uber-eats-data-scraping-services/", views.uber_eats_data_scraping_services, name="uber_eats_data_scraping_services"),
    path("zomato-restaurant-data-scraping/", views.zomato_restaurant_data_scraping, name="zomato_restaurant_data_scraping"),

    # ======================= Social Media ======================= 
    path("facebook-data-scraping/", views.facebook_data_scraping, name="facebook_data_scraping"),
    path("instagram-data-scraping/", views.instagram_data_scraping, name="instagram_data_scraping"),
    path("linkedIn-data-scraping/", views.linkedIn_data_scraping, name="linkedIn_data_scraping"),
    path("quora-data-scraping/", views.quora_data_scraping, name="quora_data_scraping"),
    path("tikTok-data-scraping/", views.tikTok_data_scraping, name="tikTok_data_scraping"),
    path("twitter-data-scraping/", views.twitter_data_scraping, name="twitter_data_scraping"),
    path("youTube-data-scraping/", views.youTube_data_scraping, name="youTube_data_scraping"),
    path("social-media-monitoring/", views.social_media_monitoring, name="social_media_monitoring"),

    # ======================= Entertainment ======================= 
    path("streaming-OTT-platform-app-data/", views.streaming_OTT_platform_app_data, name="streaming_OTT_platform_app_data"),
    path("movie-showtime-intelligence/", views.movie_showtime_intelligence, name="movie_showtime_intelligence"),
    path("netflix-data-scraping/", views.netflix_data_scraping, name="netflix_data_scraping"),

    # ======================= Real Estate ======================= 
    path("real-estate-data-intelligence/", views.real_estate_data_intelligence, name="real_estate_data_intelligence"),
    path("zillow-data-scraping/", views.zillow_data_scraping, name="zillow_data_scraping"),
    path("realtor-data-scraping/", views.realtor_data_scraping, name="realtor_data_scraping"),
    path("housing-data-scraping/", views.housing_data_scraping, name="housing_data_scraping"),

    # ========================== Recruitment ==========================  
    path("job-listings-and-data-feeds/", views.job_listings_and_data_feeds, name="job_listings_and_data_feeds"),
    path("human-capital-management/", views.human_capital_management, name="human_capital_management"),

    # ========================== News & Media ==========================
    path("news-aggregation-and-intelligence/", views.news_aggregation_and_intelligence, name="news_aggregation_and_intelligence"),
    path("data-for-research-and-journalism-scraping/", views.data_for_research_and_journalism_scraping, name="data_for_research_and_journalism_scraping"),

    # ========================== Finance ==========================  
    path("stock-market-and-financial-data-scraping/", views.stock_market_and_financial_data_scraping, name="stock_market_and_financial_data_scraping"),
    path("alternative-data/", views.alternative_data, name="alternative_data"),

    # ========================== Data Aggregation ==========================  
    path("data-intelligence/", views.data_intelligence, name="data_intelligence"),
    path("location-intelligence/", views.location_intelligence, name="location_intelligence"),
    path("customer-intelligence/", views.customer_intelligence, name="customer_intelligence"),
    path("sales-intelligence/", views.sales_intelligence, name="sales_intelligence"),
]