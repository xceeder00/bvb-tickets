#!/usr/bin/env python3
"""
Test script for Telegram bot integration
"""

import requests
import json
import os

def test_telegram_bot():
    """Test Telegram bot configuration and send a test message."""
    
    # Try to load config from file first
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        telegram_config = config.get('telegram', {})
        bot_token = telegram_config.get('bot_token')
        chat_id = telegram_config.get('chat_id')
        
    except FileNotFoundError:
        print("❌ config.json not found, trying environment variables...")
        bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
        chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    if not bot_token or not chat_id:
        print("❌ ERROR: Missing Telegram credentials!")
        print("Please set bot_token and chat_id in config.json or as environment variables")
        print("\nExample config.json:")
        print(json.dumps({
            "telegram": {
                "enabled": True,
                "bot_token": "123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ",
                "chat_id": "123456789"
            }
        }, indent=2))
        return False
    
    print("🤖 Testing Telegram bot...")
    print(f"Bot Token: {bot_token[:10]}...")
    print(f"Chat ID: {chat_id}")
    
    # Test message
    message = """🧪 *Test Message* 🧪

This is a test from your BVB Ticket Monitor!

✅ Bot is working correctly
🤖 Ready to monitor for tickets
🎫 You'll be notified when tickets are available

*Setup Complete!* 🎉"""
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }
        
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        
        print("✅ SUCCESS: Test message sent!")
        print("Check your Telegram to see the test message.")
        return True
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        if response.status_code == 401:
            print("❌ Unauthorized - Check your bot token")
        elif response.status_code == 400:
            print("❌ Bad Request - Check your chat ID")
        else:
            print(f"❌ Response: {response.text}")
        return False
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def test_bot_info(bot_token):
    """Test bot token by getting bot info."""
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        bot_info = response.json()
        if bot_info.get('ok'):
            bot_data = bot_info.get('result', {})
            print(f"✅ Bot Info: {bot_data.get('first_name')} (@{bot_data.get('username')})")
            return True
        else:
            print(f"❌ Bot API Error: {bot_info}")
            return False
            
    except Exception as e:
        print(f"❌ Failed to get bot info: {e}")
        return False

if __name__ == "__main__":
    print("🎫 BVB Ticket Monitor - Telegram Test")
    print("=" * 40)
    
    success = test_telegram_bot()
    
    if success:
        print("\n🎉 All tests passed!")
        print("Your Telegram bot is ready for ticket monitoring.")
    else:
        print("\n❌ Tests failed!")
        print("Please check your configuration and try again.")
        print("\nNeed help? Check telegram_setup.md for detailed instructions.")
