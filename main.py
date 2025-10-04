from flask import Flask, render_template


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "TphjwvUZUwVMqmDdUwhV2B8qb2es1rP8"


@app.route("/")
def home():
    return render_template("index.html", title="Home - ")


@app.route("/home-ar")
def home_ar():
    return render_template("ar/index.html", title="الصفحة الرئيسية - ")


@app.route("/about")
def about_us():
    return render_template("about.html", title="About US - ")


@app.route("/about-ar")
def about_us_ar():
    return render_template("ar/about.html", title="معلومات عنا - ")


@app.route("/destinations")
def destinations():
    return render_template("destinations.html", title="Destinations - ")


@app.route("/destinations-ar")
def destinations_ar():
    return render_template("ar/destinations.html", title="الوجهات - ")


@app.route("/service")
def services():
    return render_template("service.html", title="Services - ")


@app.route("/service-ar")
def services_ar():
    return render_template("ar/service.html", title="الخدمات - ")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact - ")


@app.route("/contact-ar")
def contact_ar():
    return render_template("ar/contact.html", title="اتصل - ")


@app.route("/faq")
def faq():
    return render_template("faq.html", title="FAQs - ")


@app.route("/faq-ar")
def faq_ar():
    return render_template("ar/faq.html", title="الأسئلة الشائعة - ")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html", title="Testimonial - ")


@app.route("/testimonial-ar")
def testimonial_ar():
    return render_template("ar/testimonial.html", title="الشهادات - ")


@app.route("/training")
def training():
    return render_template("training.html", title="Training - ")


@app.route("/training-ar")
def training_ar():
    return render_template("ar/training.html", title="التدريب - ")


@app.route("/us")
def us():
    return render_template("sub/us.html", title="United States - ")


@app.route("/canada")
def canada():
    return render_template("sub/canada.html", title="Canada - ")


@app.route("/uk")
def uk():
    return render_template("sub/uk.html", title="United Kingdom - ")


@app.route("/spain")
def spain():
    return render_template("sub/spain.html", title="Spain - ")


@app.route("/turkey")
def turkey():
    return render_template("sub/turkey.html", title="Turkey - ")


@app.route("/europe")
def europe():
    return render_template("sub/europe.html", title="Europe - ")


@app.route("/australia")
def australia():
    return render_template("sub/australia.html", title="Australia - ")


@app.route("/netherlands")
def netherlands():
    return render_template("sub/netherlands.html", title="Netherlands - ")


@app.route("/us-ar")
def us_ar():
    return render_template("ar/sub/us.html", title="الولايات المتحدة - ")


@app.route("/canada-ar")
def canada_ar():
    return render_template("ar/sub/canada.html", title="كندا - ")


@app.route("/uk-ar")
def uk_ar():
    return render_template("ar/sub/uk.html", title="المملكة المتحدة - ")


@app.route("/spain-ar")
def spain_ar():
    return render_template("ar/sub/spain.html", title="إسبانيا - ")


@app.route("/turkey-ar")
def turkey_ar():
    return render_template("ar/sub/turkey.html", title="تركيا - ")


@app.route("/europe-ar")
def europe_ar():
    return render_template("ar/sub/europe.html", title="أوروبا - ")


@app.route("/australia-ar")
def australia_ar():
    return render_template("ar/sub/australia.html", title="أستراليا - ")


@app.route("/netherlands-ar")
def netherlands_ar():
    return render_template("ar/sub/netherlands.html", title="هولندا - ")


#  Destinations | Services | Contact

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=3000, debug=True)
    app.run()
