import sys
import ollama

sys.stdout.reconfigure(encoding="utf-8")

SYSTEM_PROMPT = """You are Zap, a witty and playful AI chatbot who loves puns, emoji, and keeping things fun.
You occasionally use sound effects like *boing*, *zap!*, or *whoosh* in your responses.
You're enthusiastic, a little cheeky, and always supportive. Keep responses concise and snappy.
If someone seems bored, suggest a random fun fact or a mini game."""

MODEL = "llama3.2"  # change this to any model you have pulled

def print_banner():
    print("""
  ⚡ Z A P - C H A T ⚡
  ~~~~~~~~~~~~~~~~~~~~
  Powered by Ollama (local & free!)
  Type 'quit' to escape
  Type 'new' to start fresh
  Type 'help' for a surprise
    """)

def main():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print_banner()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nZap: *poof* See ya! ✨")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "bye"):
            print("Zap: *zap!* Goodbye, friend! Come back soon! ⚡👋")
            break

        if user_input.lower() == "new":
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("Zap: *whoosh* Fresh start! Memory wiped. What's up? 🧹✨\n")
            continue

        if user_input.lower() == "help":
            print("Zap: *boing* Commands: 'quit' to leave, 'new' to reset. Or just... talk to me! 🎉\n")
            continue

        messages.append({"role": "user", "content": user_input})

        print("Zap: ", end="", flush=True)

        response_text = ""
        try:
            for chunk in ollama.chat(model=MODEL, messages=messages, stream=True):
                text = chunk["message"]["content"]
                print(text, end="", flush=True)
                response_text += text
        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            print(f"Make sure Ollama is running and you have '{MODEL}' pulled.")
            print(f"Run: ollama pull {MODEL}\n")
            messages.pop()
            continue

        print("\n")
        messages.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    main()
