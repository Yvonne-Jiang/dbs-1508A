#!/usr/bin/env python
# coding: utf-8

# In[55]:


from flask import Flask, render_template, request
import joblib


# In[59]:


app = Flask(__name__)


# In[60]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return render_template("index.html", results1=r1, results2=r2)
    else:
        return render_template("index.html", results1="waiting", results2="waiting")


# In[61]:


if __name__ == "__main__":
    app.run(host="localhost", port=8000)


# In[ ]:




