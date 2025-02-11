Below is an example README file for your project:

------------------------------------------------------------
Project Title: Autism Risk Assessment for Babies

Overview:
-------------
This project is a web-based application that assesses autism risk in babies using a series of behavioral questions. The interface collects user responses and displays an assessment result. In addition, the website offers an interactive dark mode toggle, allowing users to switch between light and dark themes. The dark mode preference is saved in the browser so that the selected theme persists throughout user sessions.

Features:
-------------
• Two-step assessment form with behavioral questions for babies (0–6 months and 6–12 months).  
• Dynamic result page that displays low or high autism risk messages.  
• A responsive, clean design with a modern UI.  
• Dark mode integration with an easy toggle button.  
• User’s theme preference is stored using localStorage for a persistent experience.

Project Structure:
-------------
├── static  
│   ├── css  
│   │   └── styles.css         // Contains both light mode and dark mode CSS  
│   └── js  
│       └── theme.js           // Handles the dark/light theme toggle and persistence  
├── templates  
│   ├── index.html           // Main page with the assessment form and dark mode toggle  
│   └── result.html          // Result page that shows the autism risk message and dark mode toggle  
└── README.md                // This file

Installation:
-------------
1. Clone or download the project repository.  
2. Ensure the project is served on a web server. (For example, if using Flask, the templates folder can be automatically loaded and the static folder will be referenced accordingly.)  

Example using Flask:
  • Install Flask:  
      pip install flask  
  • Create a main Python file (e.g., app.py) and set up your routes:
  
  --------------------------------------------------
  from flask import Flask, render_template, request
  
  app = Flask(__name__)
  
  @app.route("/")
  def index():
      return render_template("index.html")
  
  @app.route("/predict", methods=["POST"])
  def predict():
      # Process form data and determine risk...
      assessment_result = "Low Risk"  # or "High Risk"
      return render_template("result.html", result=assessment_result)
  
  if __name__ == "__main__":
      app.run(debug=True)
  --------------------------------------------------

3. Start your server and navigate to http://localhost:5000 (or your assigned port) to interact with the application.

Usage:
-------------
• Open the application in your web browser.  
• Answer the behavioral questions and click the “Assess Risk” button to get the result.  
• Toggle between dark and light mode using the provided switch at the top-right corner on both pages.  
• The chosen theme is automatically saved and will persist even after page refreshes.

Customization:
-------------
• You can easily modify the styles in static/css/styles.css for further customization.  
• The dark mode colors are defined using the data-theme attribute on the <body> tag.
• Adjust or add new questions by editing the HTML forms in index.html.

License:
-------------
This project is distributed for educational purposes. You are free to improve, modify, or use this code for public or private projects.

Contact:
-------------
For additional questions, issues, or contributions, please contact the project maintainer or submit an issue on the repository.

------------------------------------------------------------
This README provides a complete overview of your project, instructions for installation, usage guidelines, and customization options. Feel free to update any sections if your project grows or new features are introduced.