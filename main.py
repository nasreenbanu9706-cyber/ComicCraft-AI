from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import os

app = FastAPI()
stories = []

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/generate", response_class=HTMLResponse)
async def generate(story: str = Form(...)):
    stories.append(story)
    lower = story.lower()

    if "cat" in lower and "dog" in lower:
        p1_emoji, p1_text = "🐱", "Oru chinna oor la cute Cat Mittu irunthuchu"
        p2_emoji, p2_text = "🐶", "Pakkathula Dog Bruno, rendu perum sandai potukuvanga"
        p3_emoji, p3_text = "🌧️", "Periya mazhai! Cat tree la maati kituchu"
        p4_emoji, p4_text = "🤝❤️", "Dog vanthu cat-a kaapathuchu! Best friends!"
        title_emoji = "🐱🐶"
    elif "ghost" in lower:
        p1_emoji, p1_text = "🌙", "Night 12 mani paiyan thaniya"
        p2_emoji, p2_text = "😱", "Thideernu sound! Yaaro pinaadi?"
        p3_emoji, p3_text = "👻", "Cute ghost! Bayam illa"
        p4_emoji, p4_text = "👦👻", "Ghost ku friend kidaichiduchu!"
        title_emoji = "👻"
    else:
        p1_emoji, p1_text = "⭐", f"Story start! {story}"
        p2_emoji, p2_text = "⚡", "Periya problem vanthuchu!"
        p3_emoji, p3_text = "💪", "Hero fight panni jaikaran!"
        p4_emoji, p4_text = "🎉", "Happy Ending!"
        title_emoji = "✨"

    # Create printable HTML with download button
    return f"""
    <html>
    <head><meta charset="UTF-8"><title>Comic</title></head>
    <body style="background:#0a0a0a; color:white; padding:20px; font-family:sans-serif;">
    <center><h1 style="color:#ff0055;">Comic Ready da! 🔥</h1>
    <h2>{title_emoji} {story}</h2></center>
    
    <div id="comic-content" style="max-width:600px; margin:auto; border:3px solid #ff0055; padding:20px; border-radius:15px; background:#1a1a1a;">
        <div style="background:#222; margin:15px 0; padding:20px; border-radius:12px; text-align:center;">
            <div style="font-size:80px;">{p1_emoji}</div>
            <p><b>Panel 1:</b> {p1_text}</p>
        </div>
        <div style="background:#222; margin:15px 0; padding:20px; border-radius:12px; text-align:center;">
            <div style="font-size:80px;">{p2_emoji}</div>
            <p><b>Panel 2:</b> {p2_text}</p>
        </div>
        <div style="background:#222; margin:15px 0; padding:20px; border-radius:12px; text-align:center;">
            <div style="font-size:80px;">{p3_emoji}</div>
            <p><b>Panel 3:</b> {p3_text}</p>
        </div>
        <div style="background:#222; margin:15px 0; padding:20px; border-radius:12px; text-align:center;">
            <div style="font-size:80px;">{p4_emoji}</div>
            <p><b>Panel 4:</b> {p4_text}</p>
        </div>
        <p style="text-align:center; color:#ff0055; font-weight:bold; font-size:20px;">THE END ❤️</p>
    </div>

    <br><center>
        <!-- DOWNLOAD BUTTON - ITHU THAAN MUKKIYAM -->
        <button onclick="downloadPDF()" style="background:#0044ff; color:white; padding:15px 30px; font-size:18px; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">
            📥 Download Your Comic as PDF
        </button>
        <br><br>
        <a href="/" style="color:#00ffcc;">Home ku po da</a> | 
        <a href="/all-users" style="color:#00ffcc;">All Stories</a>
    </center>

    <script>
    function downloadPDF() {{
        var content = document.getElementById('comic-content').innerHTML;
        var win = window.open('', '', 'height=700,width=800');
        win.document.write('<html><head><title>Comic PDF</title><meta charset="UTF-8"></head><body style="font-family:sans-serif; padding:20px;">');
        win.document.write('<h1 style="text-align:center;">{story}</h1>');
        win.document.write(content);
        win.document.write('</body></html>');
        win.document.close();
        win.print();
    }}
    </script>

    </body>
    </html>
    """

@app.get("/all-users", response_class=HTMLResponse)
async def all_users():
    items = "".join([f"<li style='margin:10px; padding:10px; border:1px solid #ff0055; border-radius:8px;'>{s}</li>" for s in stories]) if stories else "<p>Yarum story type pannala da!</p>"
    return f"<html><head><meta charset='UTF-8'></head><body style='background:#0a0a0a; color:white; padding:30px;'><h1 style='color:#ff0055;'>Ellarum Stories</h1><ul style='list-style:none;'>{items}</ul><br><a href='/' style='color:#00ffcc;'>Home ku po da</a></body></html>"