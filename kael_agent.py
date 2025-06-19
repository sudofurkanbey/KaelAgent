import os
import openai

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

print("\n🔁 KaelAgent v0.3 has started.")

while True:
    command = input("\nEnter command (type 'exit' to quit): ").strip()
    
    if command == 'exit':
        print("\n👋 Exiting KaelAgent...")
        break

    # Shortcuts
    if command == "pub":
        command = "flutter pub get"
    elif command == "doctor":
        command = "flutter doctor"
    elif command == "build":
        command = "flutter build apk"

    print(f"\n▶ Executing: {command}\n")
    try:
        output = os.popen(command).read()
        print(output)

        if "Error" in output or "FAILURE" in output or "Exception" in output:
            print("\n⛔ ERROR DETECTED. Sending to GPT-4 for analysis...")

            gpt_response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": (
                            "You are a debugging assistant. Analyze terminal, Python, and Flutter errors "
                            "and provide a clear fix command. ONLY return the fix – no extra explanations."
                        )
                    },
                    {"role": "user", "content": output}
                ]
            )

            suggestion = gpt_response.choices[0].message.content
            print(f"\n💡 GPT Suggestion:\n{suggestion}")

            apply = input("\n🛠️ Apply suggestion? (y/n): ").strip().lower()
            if apply == 'y':
                print("\n▶ Applying GPT suggestion...")
                os.system(suggestion)
            else:
                print("⏭️ Skipped.")
    
    except Exception as e:
        print(f"❌ Runtime Error: {e}")
