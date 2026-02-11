import streamlit.components.v1 as components

def render_voice_controls():
    components.html("""
    <h4>🎙️ Speak Your Prompt</h4>
    <button onclick="startDictation()">Start Dictation</button>
    <script>
    function startDictation() {
      var recognition = new webkitSpeechRecognition();
      recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        alert("You said: " + transcript);
      };
      recognition.start();
    }
    </script>
    """, height=150)

    components.html("""
    <h4>🔊 Read Aloud</h4>
    <button onclick="speak()">Play Last Reply</button>
    <script>
    function speak() {
      var msg = new SpeechSynthesisUtterance("Soulvest is here to guide you.");
      window.speechSynthesis.speak(msg);
    }
    </script>
    """, height=150)

def render_voice_button(text, key="voice"):
    safe_text = text.replace('"', "'").replace("\n", " ")
    components.html(f"""
    <button onclick="speak_{key}()">🔊 Read Aloud</button>
    <script>
    function speak_{key}() {{
      var msg = new SpeechSynthesisUtterance("{safe_text}");
      window.speechSynthesis.speak(msg);
    }}
    </script>
    """, height=100)
