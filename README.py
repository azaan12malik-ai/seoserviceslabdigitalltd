from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEO Services Lab Digital Ltd</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Your CSS (same as in your HTML) */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
        }
        header {
            background-color: #007bff;
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 2.5em;
        }
        header p {
            font-size: 1.2em;
            margin: 10px 0 0;
        }
        .hero {
            background-image: linear-gradient(rgba(0,123,255,0.8), rgba(0,123,255,0.8)), url('https://via.placeholder.com/1200x400?text=Digital+Marketing+Hero+Image');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 100px 20px;
            text-align: center;
        }
        .hero h2 {
            font-size: 2em;
            margin-bottom: 20px;
        }
        .hero p {
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .hero a {
            background-color: white;
            color: #007bff;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .about-us, .why-choose, .testimonials, .process {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        .about-us h2, .why-choose h2, .testimonials h2, .process h2 {
            color: #007bff;
            text-align: center;
        }
        .why-choose ul {
            list-style-type: none;
            padding: 0;
        }
        .why-choose li {
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
        }
        .why-choose li::before {
            content: "✓";
            color: #007bff;
            font-weight: bold;
            position: absolute;
            left: 0;
        }
        .process {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .process-step {
            text-align: center;
        }
        .process-step i {
            font-size: 3em;
            color: #007bff;
            margin-bottom: 10px;
        }
        .testimonials {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .testimonial {
            text-align: center;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 8px;
        }
        .testimonial p {
            font-style: italic;
        }
        .testimonial cite {
            font-weight: bold;
            color: #007bff;
        }
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .service {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 20px;
            text-align: center;
            transition: transform 0.3s;
        }
        .service:hover {
            transform: translateY(-5px);
        }
        .service h3 {
            margin-top: 0;
            color: #007bff;
            font-size: 1.5em;
        }
        .service i {
            font-size: 3em;
            color: #007bff;
            margin-bottom: 10px;
        }
        .contact {
            background-color: #007bff;
            color: white;
            padding: 20px;
            text-align: center;
            margin-top: 40px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
        }
        footer .footer-content {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        footer .footer-section {
            flex: 1;
            min-width: 200px;
            margin: 10px;
        }
        footer h3 {
            color: #007bff;
        }
        footer a {
            color: white;
            text-decoration: none;
        }
        footer a:hover {
            text-decoration: underline;
        }
        footer .social-icons a {
            margin: 0 10px;
            font-size: 1.5em;
        }
    </style>
</head>
<body>
    <header>
        <h1>SEO Services Lab Digital Ltd</h1>
        <p>Your Partner in Digital Marketing Excellence</p>
    </header>

    <!-- rest of your HTML code here -->
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
