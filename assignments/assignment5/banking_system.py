# Custom Exception Classes
class InsufficientFundsError(Exception):
    """Raised when a withdrawal would result in a negative balance"""
    pass

class NegativeAmountError(Exception):
    """Raised when a negative amount is provided for a transaction"""
    pass

class MaxBalanceExceededError(Exception):
    """Raised when a deposit would exceed the maximum allowed balance"""
    pass

# BankAccount Class
class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0, max_balance=100000):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.max_balance = max_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into the account"""
        try:
            # Validate amount is positive
            if amount <= 0:
                raise NegativeAmountError("Deposit amount must be positive")
            
            # Check if deposit would exceed maximum balance
            if self.balance + amount > self.max_balance:
                raise MaxBalanceExceededError(f"Deposit would exceed maximum balance of ${self.max_balance}")
            
            # Perform deposit
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            
        except NegativeAmountError as e:
            print(f"Error: {e}")
            raise
        except MaxBalanceExceededError as e:
            print(f"Error: {e}")
            raise
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        try:
            # Validate amount is positive
            if amount <= 0:
                raise NegativeAmountError("Withdrawal amount must be positive")
            
            # Check for sufficient funds
            if amount > self.balance:
                raise InsufficientFundsError(f"Insufficient funds. Current balance: ${self.balance:.2f}")
            
            # Perform withdrawal
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            
        except NegativeAmountError as e:
            print(f"Error: {e}")
            raise
        except InsufficientFundsError as e:
            print(f"Error: {e}")
            raise
    
    def transfer(self, target_account, amount):
        """Transfer money to another account"""
        try:
            # Validate amount is positive
            if amount <= 0:
                raise NegativeAmountError("Transfer amount must be positive")
            
            # Check for sufficient funds
            if amount > self.balance:
                raise InsufficientFundsError(f"Insufficient funds for transfer. Current balance: ${self.balance:.2f}")
            
            # Check if target account would exceed maximum balance
            if target_account.balance + amount > target_account.max_balance:
                raise MaxBalanceExceededError(f"Transfer would exceed target account's maximum balance of ${target_account.max_balance}")
            
            # Perform transfer
            self.balance -= amount
            target_account.balance += amount
            
            # Record transaction history
            self.transaction_history.append(f"Transferred ${amount:.2f} to account {target_account.account_number}")
            target_account.transaction_history.append(f"Received ${amount:.2f} from account {self.account_number}")
            
            print(f"Successfully transferred ${amount:.2f} to {target_account.holder_name}")
            print(f"Your new balance: ${self.balance:.2f}")
            
        except (NegativeAmountError, InsufficientFundsError, MaxBalanceExceededError) as e:
            print(f"Transfer failed: {e}")
            raise
    
    def get_balance(self):
        """Get current account balance"""
        return self.balance
    
    def get_account_info(self):
        """Display account information"""
        print(f"\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Maximum Balance: ${self.max_balance:.2f}")
    
    def show_transaction_history(self):
        """Display transaction history"""
        print(f"\n--- Transaction History for {self.holder_name} ---")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for i, transaction in enumerate(self.transaction_history, 1):
                print(f"{i}. {transaction}")

# Menu-driven interface
def main():
    """Main function with menu-driven interface"""
    accounts = {}  # Dictionary to store accounts
    
    def create_account():
        """Create a new bank account"""
        try:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print("Account number already exists!")
                return
            
            holder_name = input("Enter account holder name: ")
            
            try:
                initial_balance = float(input("Enter initial balance (default 0): ") or "0")
                max_balance = float(input("Enter maximum balance limit (default 100000): ") or "100000")
            except ValueError:
                print("Invalid amount entered. Using default values.")
                initial_balance = 0
                max_balance = 100000
            
            # Create account with exception handling
            if initial_balance < 0:
                raise NegativeAmountError("Initial balance cannot be negative")
            if initial_balance > max_balance:
                raise MaxBalanceExceededError("Initial balance exceeds maximum balance limit")
            
            account = BankAccount(account_number, holder_name, initial_balance, max_balance)
            accounts[account_number] = account
            print(f"Account created successfully for {holder_name}!")
            
        except (NegativeAmountError, MaxBalanceExceededError) as e:
            print(f"Account creation failed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def get_account():
        """Get account by account number"""
        account_number = input("Enter account number: ")
        if account_number not in accounts:
            print("Account not found!")
            return None
        return accounts[account_number]
    
    def demonstrate_exception_propagation():
        """Demonstrate exception propagation at different levels"""
        print("\n--- Exception Propagation Demonstration ---")
        
        # Create test accounts
        try:
            test_account1 = BankAccount("TEST001", "Test User 1", 1000)
            test_account2 = BankAccount("TEST002", "Test User 2", 500, 1200)
            
            print("1. Attempting to withdraw more than balance...")
            try:
                test_account1.withdraw(1500)  # This will raise InsufficientFundsError
            except InsufficientFundsError as e:
                print(f"Caught at method level: {e}")
            
            print("\n2. Attempting to deposit negative amount...")
            try:
                test_account1.deposit(-100)  # This will raise NegativeAmountError
            except NegativeAmountError as e:
                print(f"Caught at method level: {e}")
            
            print("\n3. Attempting to exceed maximum balance...")
            try:
                test_account2.deposit(800)  # This will raise MaxBalanceExceededError
            except MaxBalanceExceededError as e:
                print(f"Caught at method level: {e}")
            
            print("\n4. Demonstrating uncaught exception propagation...")
            def risky_operation():
                test_account1.withdraw(2000)  # This will propagate up
            
            try:
                risky_operation()
            except InsufficientFundsError as e:
                print(f"Caught at higher level: {e}")
            
        except Exception as e:
            print(f"Caught at top level: {e}")
    
    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("           BANKING SYSTEM MENU")
        print("="*50)
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Account Information")
        print("7. Transaction History")
        print("8. Demonstrate Exception Propagation")
        print("9. Exit")
        print("="*50)
        
        try:
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == "1":
                create_account()
            
            elif choice == "2":
                account = get_account()
                if account:
                    try:
                        amount = float(input("Enter deposit amount: $"))
                        account.deposit(amount)
                    except ValueError:
                        print("Invalid amount entered!")
                    except (NegativeAmountError, MaxBalanceExceededError):
                        pass  # Error already handled in method
            
            elif choice == "3":
                account = get_account()
                if account:
                    try:
                        amount = float(input("Enter withdrawal amount: $"))
                        account.withdraw(amount)
                    except ValueError:
                        print("Invalid amount entered!")
                    except (NegativeAmountError, InsufficientFundsError):
                        pass  # Error already handled in method
            
            elif choice == "4":
                source_account = get_account()
                if source_account:
                    target_number = input("Enter target account number: ")
                    if target_number not in accounts:
                        print("Target account not found!")
                        continue
                    
                    target_account = accounts[target_number]
                    try:
                        amount = float(input("Enter transfer amount: $"))
                        source_account.transfer(target_account, amount)
                    except ValueError:
                        print("Invalid amount entered!")
                    except (NegativeAmountError, InsufficientFundsError, MaxBalanceExceededError):
                        pass  # Error already handled in method
            
            elif choice == "5":
                account = get_account()
                if account:
                    print(f"Current balance: ${account.get_balance():.2f}")
            
            elif choice == "6":
                account = get_account()
                if account:
                    account.get_account_info()
            
            elif choice == "7":
                account = get_account()
                if account:
                    account.show_transaction_history()
            
            elif choice == "8":
                demonstrate_exception_propagation()
            
            elif choice == "9":
                print("Thank you for using the Banking System!")
                break
            
            else:
                print("Invalid choice! Please enter a number between 1-9.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
