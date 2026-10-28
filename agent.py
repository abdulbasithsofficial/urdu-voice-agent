#!/usr/bin/env python3
"""UrduVoice-Agent — demo-only bilingual voice sales flow. No API calls, no keys."""
import argparse, json
FLOW = [
    ("greeting", "Assalam-o-Alaikum! Main EasyAIAgents ki AI assistant hoon. Aapke business ke liye AI agent ke baare mein baat kar sakta hoon?"),
    ("discovery", "Aapka business kis type ka hai, aur aap AI agent kis kaam ke liye chahte hain?"),
    ("qualification", "Aapki team kitni bari hai, aur ye kaam kitna urgent hai?"),
    ("objection", "Agar cost ka sawal hai, to hum pehle chhota pilot se shuru kar sakte hain, phir bara kar sakte hain."),
    ("closing", "Shukriya! Main aapki details save kar raha hoon, hamari team aapse rabta karegi."),
]
def main():
    p = argparse.ArgumentParser(); p.add_argument("--demo", action="store_true")
    p.add_argument("--business", default="example business"); p.add_argument("--urgency", default="this month")
    a = p.parse_args()
    if not a.demo:
        print("Demo mode only. Run: python3 agent.py --demo"); return
    for stage, line in FLOW:
        print(f"[{stage}] {line}")
    lead = {"business_type": a.business, "use_case": "lead qualification (demo)", "urgency": a.urgency, "team_size": "not provided in demo", "contact_details": "not provided in demo"}
    print("\nCaptured lead (demo):"); print(json.dumps(lead, indent=2, ensure_ascii=False))
if __name__ == "__main__": main()
