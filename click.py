import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")

        self.score = 0
        self.multiplier = 1
        self.auto_clicker_count = 0
        self.auto_clicker_cost = 100
        self.auto_clicker_rate = 1  # Points per second per auto-clicker
        self.multiplier_cost = 50

        # UI components
        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16))
        self.score_label.pack()

        self.click_button = tk.Button(root, text="Click me!", font=("Helvetica", 16), command=self.click)
        self.click_button.pack(pady=10)

        self.upgrade_multiplier_button = tk.Button(
            root, 
            text=f"Upgrade Multiplier (Cost: {self.multiplier_cost})", 
            font=("Helvetica", 14), 
            command=self.upgrade_multiplier, 
            state=tk.DISABLED
        )
        self.upgrade_multiplier_button.pack(pady=10)

        self.auto_clicker_button = tk.Button(
            root, 
            text=f"Buy Auto-clicker (Cost: {self.auto_clicker_cost})", 
            font=("Helvetica", 14), 
            command=self.buy_auto_clicker, 
            state=tk.DISABLED
        )
        self.auto_clicker_button.pack(pady=10)

        # Call the update function to handle UI
        self.update_ui()
        
        # Start the auto-clicker loop
        self.auto_clicker_running = False  # Track if auto-clicker loop is running

    def click(self):
        self.score += self.multiplier
        self.update_ui()

    def upgrade_multiplier(self):
        if self.score >= self.multiplier_cost:
            self.score -= self.multiplier_cost
            self.multiplier += 1
            self.multiplier_cost = int(self.multiplier_cost * 1.5)  # Increase by 50%
        self.update_ui()

    def buy_auto_clicker(self):
        if self.score >= self.auto_clicker_cost:
            self.score -= self.auto_clicker_cost
            self.auto_clicker_count += 1
            self.auto_clicker_cost = int(self.auto_clicker_cost * 1.5)  # Increase by 50%
            if not self.auto_clicker_running:
                self.start_auto_clicker()  # Start auto-clicker loop
        self.update_ui()

    def start_auto_clicker(self):
        """Begin auto-clicking logic and keep adding points based on auto-clicker count."""
        self.auto_clicker_running = True
        self.add_auto_clicker_points()
        
    def add_auto_clicker_points(self):
        """Add points to score for each auto-clicker every second."""
        if self.auto_clicker_running:
            self.score += self.auto_clicker_count * self.auto_clicker_rate
            self.update_ui()
            # Schedule next auto-clicker point update after 1 second
            self.root.after(1000, self.add_auto_clicker_points)

    def update_ui(self):
        """Update the UI elements with the current state."""
        self.score_label.config(text=f"Score: {self.score}")

        # Enable/Disable buttons based on score
        if self.score >= self.multiplier_cost:
            self.upgrade_multiplier_button.config(state=tk.NORMAL)
        else:
            self.upgrade_multiplier_button.config(state=tk.DISABLED)

        if self.score >= self.auto_clicker_cost:
            self.auto_clicker_button.config(state=tk.NORMAL)
        else:
            self.auto_clicker_button.config(state=tk.DISABLED)

        # Update button text to reflect new costs
        self.upgrade_multiplier_button.config(
            text=f"Upgrade Multiplier (Cost: {self.multiplier_cost})"
        )
        self.auto_clicker_button.config(
            text=f"Buy Auto-clicker (Cost: {self.auto_clicker_cost})"
        )


def main():
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

