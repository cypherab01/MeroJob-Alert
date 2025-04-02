# **MeroJob Scraper**

This Scrapy spider extracts IT job listings from [MeroJob](https://merojob.com) based on predefined keywords.

## **How It Works**

- Scrapes job titles and links for IT-related job postings.
- Filters results using **keywords** specified in `spiders/merojob.py`.
- Saves extracted data in **JSON format**.

## **Setup & Usage**

1. **Navigate to the project folder**:

   ```bash
   cd projects/merojob
   ```

2. **Run the spider**:
   ```bash
   scrapy runspider spiders/merojob.py -O output/jobs.json
   ```

## **Project Structure**

```
merojob/
│── spiders/
│   ├── merojob.py        # Scrapy spider script
│── output/
│   ├── jobs.json         # Scraped job listings (output)
│── README.md             # Project documentation
```

## **Customization**

- Modify the **keywords** inside `merojob.py` to scrape different job categories.
- Adjust Scrapy settings as needed.

## **License**

This project is licensed under the **MIT License**.
