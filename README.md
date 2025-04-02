# **Scrapy Spiders Collection**

This repository contains multiple **Scrapy** projects for web scraping different sources. Each project is stored inside the `projects/` directory, following a structured approach.

## **Setup Guide**

### **Prerequisites**

Ensure you have **Python** and **Scrapy** installed on your system.

1. **Install Python**: Download and install the latest version from [python.org](https://www.python.org/downloads/).
2. **Create a Virtual Environment** (recommended):
   ```bash
   python3 -m venv env
   ```
3. **Activate the Virtual Environment**:

   - **On macOS/Linux**:
     ```bash
     source env/bin/activate
     ```
   - **On Windows**:
     ```bash
     env\Scripts\activate
     ```

4. **Install Global Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Running a Scrapy Spider**

To run a spider from any project, navigate to the respective project folder and use:

```bash
scrapy runspider projects/[projectname]/spiders/[filename].py -O projects/merojob/output/output.json
```

---

## **Adding a New Scrapy Project**

1. Create a new project inside the `projects/` directory:
   ```bash
   mkdir projects/new_project
   cd projects/new_project
   ```
2. Create a `spiders/` directory inside it and add your Scrapy spider script.
3. Update `README.md` in the project folder with relevant details.

---

## **Contributing**

- Fork the repo, make changes, and submit a **pull request**.
- Follow the **project structure** for consistency.
- Use **virtual environments** to manage dependencies.

---

## **License**

This project is licensed under the MIT License.
