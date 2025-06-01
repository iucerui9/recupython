from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="ivan",
        password="NshAqGRX@2",
        database="valoracions"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dni = request.form["dni"].strip()
        poblacio = request.form["poblacio"].strip()
        valoracions = request.form["valoracions"].strip()

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO valoracions (dni, poblacio, valoracions) VALUES (%s, %s, %s)"
        cursor.execute(query, (dni, poblacio, valoracions))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

  
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM valoracions_tipus")
    valoracions = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("formulari.html", valoracions=valoracions)


@app.route("/votacions")
def votacionss():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT dni, poblacio, valoracions, fecha FROM valoracions ORDER BY fecha DESC"
        cursor.execute(query)
        votos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("votacions.html", votos=votos)
    except Exception as e:
        error_msg = f"Error al obtener las votaciones: {str(e)}"
        return render_template("votacions.html", votos=[], error=error_msg)


if __name__ == "__main__":
    app.run(debug=True)
