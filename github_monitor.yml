#!/usr/bin/env python3
"""
GitHub Actions BVB Ticket Monitor
Runs every 5 minutes via GitHub Actions cron job
"""

import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import datetime

def main():
    """Main function for GitHub Actions monitoring."""
    target_url = "https://www.ticket-onlineshop.com/ols/bvb/de/profis/channel/shop/index"
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    print(f"🔍 BVB Ticket Monitor - {datetime.now()}")
    print(f"🎯 Checking: {target_url}")
    
    if not bot_token or not chat_id:
        print("❌ ERROR: Telegram credentials not found in environment variables")
        print("Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in GitHub Secrets")
        return
    
    # Fetch the page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("📡 Fetching BVB ticket page...")
        response = requests.get(target_url, headers=headers, timeout=15)
        response.raise_for_status()
        html_content = response.text
        print("✅ Page fetched successfully")
    except requests.RequestException as e:
        print(f"❌ Failed to fetch page: {e}")
        return
    
    # Parse the page
    soup = BeautifulSoup(html_content, 'html.parser')
    
    ticket_info = {
        "empty_state_active": False,
        "tickets_available": False,
        "empty_state_found": False,
        "timestamp": datetime.now().isoformat()
    }
    
    # Check for .empty-state element and if it has .is-active class
    empty_state = soup.find(class_='empty-state')
    if empty_state:
        ticket_info["empty_state_found"] = True
        ticket_info["empty_state_active"] = 'is-active' in empty_state.get('class', [])
        print(f"🎯 Found .empty-state element, is-active: {ticket_info['empty_state_active']}")
    else:
        print("⚠️  No .empty-state element found")
    
    # If .empty-state does NOT have .is-active, tickets might be available
    if empty_state and not ticket_info["empty_state_active"]:
        ticket_info["tickets_available"] = True
        print("🎫 TICKETS DETECTED: .empty-state does not have .is-active class!")
        
        # Send Telegram notification
        send_telegram_notification(bot_token, chat_id, ticket_info, target_url)
    else:
        print("📋 No tickets available yet")
    
    # Log results
    log_entry = {
        "timestamp": ticket_info["timestamp"],
        "empty_state_found": ticket_info["empty_state_found"],
        "empty_state_active": ticket_info["empty_state_active"],
        "tickets_available": ticket_info["tickets_available"]
    }
    
    # Write to log file
    with open('monitor.log', 'a') as f:
        f.write(f"{json.dumps(log_entry)}\n")
    
    print(f"📊 Status: Empty State Active: {ticket_info['empty_state_active']}")
    print(f"🎫 Tickets Available: {ticket_info['tickets_available']}")
    print("✅ Monitor check completed")

def send_telegram_notification(bot_token, chat_id, ticket_info, target_url):
    """Send Telegram notification about ticket availability."""
    try:
        message = f"""🎫 *BVB TICKETS AVAILABLE!* 🟡⚫

*October 4th Match - Act Fast!*

🕐 Detected: {ticket_info['timestamp']}
🎯 Empty State Active: {ticket_info['empty_state_active']}
📍 Status: ✅ TICKETS AVAILABLE!

🔗 [Buy Tickets NOW!]({target_url})

⚡ Don't wait - tickets sell out fast!
🤖 Monitored via GitHub Actions
"""
        
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown',
            'disable_web_page_preview': False
        }
        
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        print("📱 Telegram notification sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send Telegram message: {e}")
        return False

if __name__ == "__main__":
    main()
