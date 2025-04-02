import scrapy

class MeroJobSpider(scrapy.Spider):
    name = "merojob"
    start_urls = [
        "https://merojob.com/search/?q=&job_category=111&expiring_status=&start_date=&end_date=&page=1"
    ]

    base_url = "https://merojob.com"

    def parse(self, response):
        jobs = response.css('div.card.mt-3.hover-shadow')
        for job in jobs:
            job_link = self.base_url + job.css("h1.text-primary.font-weight-bold.media-heading.h4 a::attr(href)").get(default="")

            yield response.follow(job_link, callback=self.parse_job_detail, meta={'job_link': job_link})

        # Handle pagination
        next_page = response.css('a.pagination-next.page-link::attr(href)').get()
        if next_page:
            yield response.follow(self.base_url + next_page, callback=self.parse)

    def parse_job_detail(self, response):
        keywords = ["next.js", 
         "react", 
         "react native", 
         'react-native', 
         'frontend developer', 
         'full stack developer',
         'nextjs',
         'nextjs developer',
         'react developer',
         ]
        raw_text = response.css("div.card *::text").getall()
        cleaned_text = [text.strip().replace("\xa0", " ") for text in raw_text if text.strip()]
        
        # Join all text into a single string for easier searching
        full_description = " ".join(cleaned_text).lower()
        
        # Check if any keyword is in the description (case-insensitive)
        if any(keyword.lower() in full_description for keyword in keywords):
            yield {
                'title': response.css('h1.h4.mb-0.text-primary::text').get(),
                'job_link': response.meta['job_link'],
            }
