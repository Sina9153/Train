import tkinter as tk
from tkinter import messagebox
import requests
import time
import json
import threading


# =========================
# COLORS
# =========================

BG = "#0f172a"
CARD = "#1e293b"
INPUT = "#334155"
TEXT = "#f8fafc"
MUTED = "#94a3b8"
ACCENT = "#38bdf8"
GREEN = "#22c55e"
RED = "#ef4444"


# =========================
# API CHECK
# =========================

def check_api():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning(
            "Warning",
            "Please enter a URL."
        )
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Clear previous result
    result_box.delete("1.0", tk.END)

    status_label.config(
        text="● Connecting...",
        fg=ACCENT
    )

    # Disable button while request is running
    check_button.config(state="disabled")

    # Run request in background
    thread = threading.Thread(
        target=make_request,
        args=(url,),
        daemon=True
    )

    thread.start()


def make_request(url):
    try:
        start = time.perf_counter()

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Sina-API-Explorer/1.0",
                "Accept": "application/json"
            }
        )

        elapsed = time.perf_counter() - start

        # Prepare response information
        result = (
            "╔════════════════════════════════════╗\n"
            "║          API EXPLORER              ║\n"
            "╚════════════════════════════════════╝\n\n"
        )

        result += f"🌐 URL\n{url}\n\n"

        result += f"📊 Status Code : {response.status_code}\n"
        result += f"📋 Status      : {response.reason}\n"
        result += f"⚡ Response    : {elapsed:.3f} seconds\n"
        result += f"📦 Size        : {len(response.content):,} bytes\n"
        result += f"🔤 Encoding    : {response.encoding}\n\n"

        result += (
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📨 RESPONSE HEADERS\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

        for key, value in response.headers.items():
            result += f"{key}: {value}\n"

        result += (
            "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🧠 RESPONSE DATA\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

        # Try to parse JSON
        try:
            data = response.json()

            result += json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            )

        except ValueError:
            # Not JSON
            result += response.text[:3000]

        # Update GUI from main thread
        root.after(
            0,
            show_success_result,
            result,
            response.status_code
        )

    except requests.exceptions.Timeout:

        root.after(
            0,
            show_error,
            "● Timeout",
            RED,
            "Timeout",
            "The server didn't respond within 10 seconds."
        )

    except requests.exceptions.ConnectionError:

        root.after(
            0,
            show_error,
            "● Connection failed",
            RED,
            "Connection Error",
            "Could not connect to the server."
        )

    except requests.exceptions.RequestException as error:

        root.after(
            0,
            show_error,
            "● Request error",
            RED,
            "Request Error",
            str(error)
        )

    except Exception as error:

        root.after(
            0,
            show_error,
            "● Unexpected error",
            RED,
            "Unexpected Error",
            str(error)
        )


# =========================
# SHOW SUCCESS RESULT
# =========================

def show_success_result(result, status_code):

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        result
    )

    result_box.see("1.0")

    # Status message
    if 200 <= status_code < 300:

        status_label.config(
            text="● Request successful",
            fg=GREEN
        )

    elif status_code >= 400:

        status_label.config(
            text="● Server returned an error",
            fg=RED
        )

    else:

        status_label.config(
            text="● Request completed",
            fg=ACCENT
        )

    check_button.config(
        state="normal"
    )


# =========================
# SHOW ERROR
# =========================

def show_error(
    status_text,
    status_color,
    title,
    message
):

    status_label.config(
        text=status_text,
        fg=status_color
    )

    check_button.config(
        state="normal"
    )

    messagebox.showerror(
        title,
        message
    )


# =========================
# FEATURES WINDOW
# =========================

def show_features():

    features = tk.Toplevel(root)

    features.title("Program Features")
    features.geometry("550x500")
    features.minsize(450, 400)
    features.configure(bg=BG)

    title = tk.Label(
        features,
        text="🚀 API EXPLORER",
        font=("Segoe UI", 24, "bold"),
        bg=BG,
        fg=ACCENT
    )

    title.pack(
        pady=(30, 10)
    )

    subtitle = tk.Label(
        features,
        text="What can this program do?",
        font=("Segoe UI", 12),
        bg=BG,
        fg=MUTED
    )

    subtitle.pack()

    feature_text = """
  ✓ Check any HTTP/HTTPS URL

  ✓ Show HTTP status codes

  ✓ Measure server response time

  ✓ Calculate response size

  ✓ Display response headers

  ✓ Read and format JSON responses

  ✓ Show text responses

  ✓ Handle connection errors

  ✓ Handle request timeouts

  ✓ Automatically detect JSON responses

  ✓ Beautiful graphical interface

  ✓ Non-blocking background requests

  ✓ Built with Python + Tkinter + Requests
"""

    box = tk.Label(
        features,
        text=feature_text,
        justify="left",
        anchor="w",
        font=("Segoe UI", 12),
        bg=CARD,
        fg=TEXT,
        padx=30,
        pady=25
    )

    box.pack(
        padx=30,
        pady=30,
        fill="both",
        expand=True
    )


# =========================
# CLEAR RESULT
# =========================

def clear_result():

    url_entry.delete(
        0,
        tk.END
    )

    result_box.delete(
        "1.0",
        tk.END
    )

    url_entry.insert(
        0,
        "https://jsonplaceholder.typicode.com/users/1"
    )

    status_label.config(
        text="● Ready",
        fg=GREEN
    )


# =========================
# ENTER KEY
# =========================

def enter_pressed(event):
    check_api()


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title("API Explorer")
root.geometry("900x700")
root.minsize(750, 600)
root.configure(bg=BG)


# =========================
# HEADER
# =========================

header = tk.Frame(
    root,
    bg=BG
)

header.pack(
    fill="x",
    padx=35,
    pady=(25, 10)
)


title = tk.Label(
    header,
    text="API Explorer",
    font=("Segoe UI", 30, "bold"),
    bg=BG,
    fg=TEXT
)

title.pack(
    anchor="w"
)


subtitle = tk.Label(
    header,
    text="Powerful HTTP / API analyzer built with Python",
    font=("Segoe UI", 11),
    bg=BG,
    fg=MUTED
)

subtitle.pack(
    anchor="w"
)


# =========================
# URL CARD
# =========================

card = tk.Frame(
    root,
    bg=CARD
)

card.pack(
    fill="x",
    padx=35,
    pady=15
)


url_label = tk.Label(
    card,
    text="🌐 API / Website URL",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=TEXT
)

url_label.pack(
    anchor="w",
    padx=20,
    pady=(18, 7)
)


url_entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    bg=INPUT,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)

url_entry.pack(
    fill="x",
    padx=20,
    ipady=10
)

url_entry.insert(
    0,
    "https://jsonplaceholder.typicode.com/users/1"
)


# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(
    card,
    bg=CARD
)

button_frame.pack(
    fill="x",
    padx=20,
    pady=15
)


check_button = tk.Button(
    button_frame,
    text="🚀 Check API",
    command=check_api,
    font=("Segoe UI", 11, "bold"),
    bg=ACCENT,
    fg="#020617",
    activebackground="#7dd3fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)

check_button.pack(
    side="left",
    padx=(0, 10)
)


clear_button = tk.Button(
    button_frame,
    text="🧹 Clear",
    command=clear_result,
    font=("Segoe UI", 11),
    bg=INPUT,
    fg=TEXT,
    activebackground="#475569",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)

clear_button.pack(
    side="left"
)


features_button = tk.Button(
    button_frame,
    text="❓ What can it do?",
    command=show_features,
    font=("Segoe UI", 11),
    bg=INPUT,
    fg=TEXT,
    activebackground="#475569",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)

features_button.pack(
    side="right"
)


# =========================
# STATUS
# =========================

status_label = tk.Label(
    root,
    text="● Ready",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=GREEN
)

status_label.pack(
    anchor="w",
    padx=35,
    pady=(5, 5)
)


# =========================
# RESULT BOX
# =========================

result_frame = tk.Frame(
    root,
    bg=CARD
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=(5, 25)
)


result_box = tk.Text(
    result_frame,
    font=("Consolas", 10),
    bg="#020617",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    wrap="word"
)

result_box.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# =========================
# KEYBOARD SHORTCUT
# =========================

url_entry.bind(
    "<Return>",
    enter_pressed
)


# Put cursor in URL field
url_entry.focus()


# =========================
# START PROGRAM
# =========================

root.mainloop()
