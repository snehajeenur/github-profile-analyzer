from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_data = None
    error = None

    if request.method == "POST":
        username = request.form["username"]
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            user_data = {
                "name": data.get("name"),
                "bio": data.get("bio"),
                "repos": data.get("public_repos"),
                "followers": data.get("followers"),
                "following": data.get("following"),
                "profile_url": data.get("html_url"),
                "created_at": data.get("created_at"),
                "avatar": data.get("avatar_url")
            }
        else:
            error = "User not found"

    return render_template("index.html", user=user_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
