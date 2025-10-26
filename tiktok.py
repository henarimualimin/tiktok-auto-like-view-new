import requests
import time
import random
from datetime import datetime
import os
import re

class TikTokAutoBot:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://socioblend.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
            'Origin': self.base_url,
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.username = None
        self.tiktok_url = None
        self.email = None
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = """
\033[1;36m
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║  \033[1;33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\033[1;36m  ║
║  \033[1;33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\033[1;36m  ║
║  \033[1;33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ \033[1;37m🛰️  AIRDROPDIGGERID \033[1;33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\033[1;36m  ║
║  \033[1;33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\033[1;36m  ║
║  \033[1;33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\033[1;36m  ║
║                                                                ║
║        \033[1;32m🚀 TIKTOK AUTO BOT MULTI-FEATURE 🚀\033[1;36m             ║
║              \033[1;35mPowered by AirdropDigger\033[1;36m                    ║
╚════════════════════════════════════════════════════════════════╝
\033[0m
        """
        print(banner)
    
    def print_menu(self):
        menu = """
\033[1;36m
🎮 SELECT MENU 🎮

\033[1;32m[1] TikTok Auto View\033[0m
\033[1;33m[2] TikTok Auto Likes\033[0m  
\033[1;31m[0] Exit\033[0m
"""
        print(menu)
    
    def print_waiting(self, minutes, seconds=0):
        arrows = ["↗", "↘", "↙", "↖", "→", "←", "↑", "↓"]
        arrow = random.choice(arrows)
        if seconds > 0:
            time_str = f"{minutes:02d}:{seconds:02d}"
        else:
            time_str = f"{minutes} minutes"
        print(f"\033[1;35m{arrow} \033[1;33mWaiting {time_str}... {arrow}\033[0m")
    
    def get_csrf_token(self, page_url):
        """Get fresh CSRF token from the specified page"""
        try:
            self.headers['Referer'] = page_url
            response = self.session.get(
                page_url,
                headers=self.headers
            )
            
            # Extract CSRF token using regex
            csrf_match = re.search(r'name="csrf"\s+value="([a-f0-9]+)"', response.text)
            if csrf_match:
                csrf_token = csrf_match.group(1)
                print(f"\033[1;32m✅ CSRF Token obtained: {csrf_token}\033[0m")
                return csrf_token
            else:
                print("\033[1;31m❌ CSRF Token not found in page\033[0m")
                return None
                
        except Exception as e:
            print(f"\033[1;31m❌ Error getting CSRF token: {e}\033[0m")
            return None

    # ==============================
    # MENU 1: TIKTOK AUTO VIEW
    # ==============================
    
    def get_auto_view_input(self):
        """Get user input for auto view"""
        print("\033[1;36m" + "="*60 + "\033[0m")
        print("\033[1;33m🎯 TIKTOK AUTO VIEW - Enter your details:\033[0m")
        
        self.username = input("\033[1;36m📝 Enter TikTok username @: \033[0m").strip()
        self.tiktok_url = input("\033[1;36m🔗 Enter TikTok video URL: \033[0m").strip()
        
        print("\033[1;36m" + "="*60 + "\033[0m")
        print(f"\033[1;32m✅ Data saved - Username: {self.username}\033[0m")
        print(f"\033[1;32m✅ Data saved - URL: {self.tiktok_url}\033[0m")
    
    def submit_view_request(self, csrf_token):
        """Submit view request with fresh CSRF token"""
        payload = {
            'csrf': csrf_token,
            'username': self.username,
            'input': self.tiktok_url
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/tiktok/ftv/api/claim.php",
                data=payload,
                headers=self.headers
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('ok'):
                    print(f"\033[1;32m🎉 Successfully claimed views!\033[0m")
                    print(f"\033[1;36m📹 Video ID: {result.get('video_id')}\033[0m")
                    print(f"\033[1;35m🔑 Token: {result.get('token')}\033[0m")
                    return True
                else:
                    print(f"\033[1;31m❌ Claim failed: {result}\033[0m")
                    return False
            else:
                print(f"\033[1;31m❌ HTTP Error: {response.status_code}\033[0m")
                return False
                
        except Exception as e:
            print(f"\033[1;31m❌ Error submitting request: {e}\033[0m")
            return False

    def run_auto_view_claim(self):
        """Run auto view claim cycle with fresh CSRF token"""
        print(f"\n\033[1;34m🔄 Starting auto-view claim cycle...\033[0m")
        print(f"\033[1;36m📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
        
        # Get fresh CSRF token from views page
        csrf_token = self.get_csrf_token(f"{self.base_url}/free-tiktok-views")
        if not csrf_token:
            print("\033[1;31m❌ Failed to get CSRF token, skipping this cycle\033[0m")
            return False
        
        # Submit view claim with fresh token
        success = self.submit_view_request(csrf_token)
        return success

    # ==============================
    # MENU 2: TIKTOK AUTO LIKES
    # ==============================
    
    def get_auto_likes_input(self):
        """Get user input for auto likes"""
        print("\033[1;36m" + "="*60 + "\033[0m")
        print("\033[1;33m🎯 TIKTOK AUTO LIKES - Enter your details:\033[0m")
        
        self.tiktok_url = input("\033[1;36m🔗 Enter TikTok video URL: \033[0m").strip()
        self.email = input("\033[1;36m📧 Enter your email: \033[0m").strip()
        
        print("\033[1;36m" + "="*60 + "\033[0m")
        print(f"\033[1;32m✅ Data saved - URL: {self.tiktok_url}\033[0m")
        print(f"\033[1;32m✅ Data saved - Email: {self.email}\033[0m")
    
    def submit_likes_request(self, csrf_token):
        """Submit likes request with fresh CSRF token"""
        payload = {
            'csrf': csrf_token,
            'tiktok-link': self.tiktok_url,
            'email': self.email
        }
        
        try:
            self.headers['Referer'] = f"{self.base_url}/free-tiktok-likes"
            response = self.session.post(
                f"{self.base_url}/tiktok/tiktokform-info.php",
                data=payload,
                headers=self.headers
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('ok'):
                    print(f"\033[1;32m🎉 Successfully claimed likes!\033[0m")
                    print(f"\033[1;36m📹 Message: {result.get('message')}\033[0m")
                    print(f"\033[1;35m🔑 Token: {result.get('token')}\033[0m")
                    return True
                else:
                    print(f"\033[1;31m❌ Claim failed: {result}\033[0m")
                    return False
            else:
                print(f"\033[1;31m❌ HTTP Error: {response.status_code}\033[0m")
                return False
                
        except Exception as e:
            print(f"\033[1;31m❌ Error submitting request: {e}\033[0m")
            return False

    def run_auto_likes_claim(self):
        """Run auto likes claim cycle with fresh CSRF token"""
        print(f"\n\033[1;34m🔄 Starting auto-likes claim cycle...\033[0m")
        print(f"\033[1;36m📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
        
        # Get fresh CSRF token from likes page
        csrf_token = self.get_csrf_token(f"{self.base_url}/free-tiktok-likes")
        if not csrf_token:
            print("\033[1;31m❌ Failed to get CSRF token, skipping this cycle\033[0m")
            return False
        
        # Submit likes claim with fresh token
        success = self.submit_likes_request(csrf_token)
        return success

    # ==============================
    # COMMON FUNCTIONS
    # ==============================
    
    def countdown_timer(self, minutes):
        """Display countdown timer with arrows"""
        total_seconds = minutes * 60
        while total_seconds > 0:
            mins = total_seconds // 60
            secs = total_seconds % 60
            self.clear_screen()
            self.print_banner()
            print(f"\033[1;34m🔄 Next auto-claim in:\033[0m")
            self.print_waiting(mins, secs)
            next_time = datetime.now().timestamp() + total_seconds
            next_time_str = datetime.fromtimestamp(next_time).strftime('%H:%M:%S')
            print(f"\033[1;36m⏰ Next claim at: {next_time_str}\033[0m")
            print("\033[1;36m" + "="*60 + "\033[0m")
            time.sleep(1)
            total_seconds -= 1

    def run_auto_view(self):
        """Run Auto View Menu"""
        self.clear_screen()
        self.print_banner()
        
        # Get initial input for auto view
        self.get_auto_view_input()
        
        print("\n\033[1;32m🎉 Auto View setup completed successfully!\033[0m")
        print("\033[1;36m🔄 Starting automatic view claims every 10 minutes...\033[0m")
        print("\033[1;33m💡 CSRF token will be refreshed automatically for each claim\033[0m")
        print("\033[1;36m" + "="*60 + "\033[0m")
        
        # Main loop - auto claim every 10 minutes
        claim_count = 1
        while True:
            try:
                print(f"\n\033[1;34m🔄 Auto-View Claim #{claim_count}\033[0m")
                self.run_auto_view_claim()
                
                claim_count += 1
                
                # Wait 10 minutes with countdown
                print(f"\n\033[1;33m⏳ Waiting 10 minutes until next auto-claim...\033[0m")
                self.countdown_timer(10)
                
                print("\033[1;32m🔄 Starting next auto-claim cycle...\033[0m")
                
            except KeyboardInterrupt:
                print("\n\n\033[1;33m👋 Returning to main menu...\033[0m")
                time.sleep(2)
                break
            except Exception as e:
                print(f"\n\033[1;31m❌ Unexpected error: {e}\033[0m")
                print("\033[1;33m🔄 Continuing in 30 seconds...\033[0m")
                time.sleep(30)

    def run_auto_likes(self):
        """Run Auto Likes Menu"""
        self.clear_screen()
        self.print_banner()
        
        # Get initial input for auto likes
        self.get_auto_likes_input()
        
        print("\n\033[1;32m🎉 Auto Likes setup completed successfully!\033[0m")
        print("\033[1;36m🔄 Starting automatic likes claims every 10 minutes...\033[0m")
        print("\033[1;33m💡 CSRF token will be refreshed automatically for each claim\033[0m")
        print("\033[1;36m" + "="*60 + "\033[0m")
        
        # Main loop - auto claim every 10 minutes
        claim_count = 1
        while True:
            try:
                print(f"\n\033[1;34m🔄 Auto-Likes Claim #{claim_count}\033[0m")
                self.run_auto_likes_claim()
                
                claim_count += 1
                
                # Wait 10 minutes with countdown
                print(f"\n\033[1;33m⏳ Waiting 10 minutes until next auto-claim...\033[0m")
                self.countdown_timer(10)
                
                print("\033[1;32m🔄 Starting next auto-claim cycle...\033[0m")
                
            except KeyboardInterrupt:
                print("\n\n\033[1;33m👋 Returning to main menu...\033[0m")
                time.sleep(2)
                break
            except Exception as e:
                print(f"\n\033[1;31m❌ Unexpected error: {e}\033[0m")
                print("\033[1;33m🔄 Continuing in 30 seconds...\033[0m")
                time.sleep(30)

    def run(self):
        """Main menu loop"""
        while True:
            try:
                self.clear_screen()
                self.print_banner()
                self.print_menu()
                
                choice = input("\033[1;36m🎯 Select menu [1/2/0]: \033[0m").strip()
                
                if choice == '1':
                    self.run_auto_view()
                elif choice == '2':
                    self.run_auto_likes()
                elif choice == '0':
                    print("\n\033[1;33m👋 Thank you for using TikTok Auto Bot! Goodbye! 👋\033[0m")
                    break
                else:
                    print("\n\033[1;31m❌ Invalid choice! Please select 1, 2, or 0.\033[0m")
                    time.sleep(2)
                    
            except KeyboardInterrupt:
                print("\n\n\033[1;33m👋 Thank you for using TikTok Auto Bot! Goodbye! 👋\033[0m")
                break
            except Exception as e:
                print(f"\n\033[1;31m❌ Unexpected error: {e}\033[0m")
                time.sleep(3)

def main():
    bot = TikTokAutoBot()
    bot.run()

if __name__ == "__main__":
    main()