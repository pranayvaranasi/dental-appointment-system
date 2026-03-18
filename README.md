# 🦷 Dental Appointment Assistant

👉 **Live App:** [https://dental-appointment-system.streamlit.app/](https://dental-appointment-system.streamlit.app/)

An AI-powered dental appointment system built with **Streamlit + LangGraph + OpenRouter**, enabling users to book, reschedule, and manage appointments through a conversational interface.

---

## 🚀 Features

* 💬 **Chat-based interface** for appointment management
* 📅 Book, cancel, and reschedule appointments
* 🧠 AI agent powered by LangGraph
* 🔌 Uses **OpenRouter** for flexible LLM access
* ⚡ Real-time streaming responses
* 📊 CSV-based lightweight backend (easy to upgrade to DB)
* 🎨 Clean SaaS-style UI with Streamlit

---

## 🧠 Example Queries

Try asking:

* “Show available slots for orthodontist”
* “Book an appointment with Dr. John Doe tomorrow”
* “Cancel my appointment”
* “Reschedule my booking”

---

## 🏗 Tech Stack

* **Frontend:** Streamlit
* **LLM Orchestration:** LangGraph
* **LLM Provider:** OpenRouter
* **Backend Logic:** LangChain tools
* **Storage:** CSV (can be upgraded to PostgreSQL/Supabase)

---

## 📦 Project Structure

```
dental-appointment-system/
│
├── streamlit_app.py        # Main UI
├── requirements.txt
├── runtime.txt            # Python version (3.11)
│
├── dental_agent/
│   ├── agent.py
│   ├── config/
│   │   └── settings.py
│   ├── tools/
│   │   ├── csv_reader.py
│   │   └── csv_writer.py
│   └── utils.py
│
└── doctor_availability.csv
```

---

## ⚙️ Setup Locally

### 1. Clone repo

```bash
git clone https://github.com/your-username/dental-appointment-system.git
cd dental-appointment-system
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add environment variables

Create `.env`:

```env
OPENROUTER_API_KEY=your_api_key_here
MODEL_NAME=openai/gpt-4o-mini
```

---

### 5. Run the app

```bash
streamlit run streamlit_app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

### Required files:

* `requirements.txt`
* `runtime.txt`

### `runtime.txt`

```txt
python-3.11
```

### Secrets (`.streamlit/secrets.toml`)

```toml
OPENROUTER_API_KEY = "your_api_key_here"
MODEL_NAME = "openai/gpt-4o-mini"
```

---

## ⚠️ Common Issues

### 1. Altair Error

```
No module named altair.vegalite.v4
```

✅ Fix:

```
altair==4.2.2
streamlit==1.32.2
```

---

### 2. Pillow / zlib Error

```
RequiredDependencyException: zlib
```

✅ Fix:

* Use `python-3.11` in `runtime.txt`

---

## 🔮 Future Improvements

* 📅 Calendar-based booking UI
* 🧾 Appointment cards instead of text
* 🔐 User authentication
* 🗄 Database integration (PostgreSQL / Supabase)
* 📊 Admin dashboard for clinics
* 📩 SMS/Email notifications

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📄 License

MIT License

---

## ❤️ Acknowledgements

* LangChain / LangGraph
* Streamlit
* OpenRouter

---

## 🌟 Demo

👉 [https://dental-appointment-system.streamlit.app/](https://dental-appointment-system.streamlit.app/)

---

