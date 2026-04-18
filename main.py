class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Transaction:
    def __init__(self, id, user_id, amount, type):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.type = type

class RiskScore:
    def __init__(self, user_id, score):
        self.user_id = user_id
        self.score = score

class BankingFraudDetectionSystem:
    def __init__(self):
        self.users = []
        self.transactions = []
        self.risk_scores = []

    def add_user(self, id, name, email):
        self.users.append(User(id, name, email))

    def add_transaction(self, id, user_id, amount, type):
        self.transactions.append(Transaction(id, user_id, amount, type))

    def calculate_risk_score(self, user_id):
        risk_score = 0
        for transaction in self.transactions:
            if transaction.user_id == user_id:
                if transaction.type == 'withdrawal' and transaction.amount > 1000:
                    risk_score += 10
                elif transaction.type == 'deposit' and transaction.amount > 5000:
                    risk_score += 5
        self.risk_scores.append(RiskScore(user_id, risk_score))

    def detect_fraud(self, user_id):
        for risk_score in self.risk_scores:
            if risk_score.user_id == user_id and risk_score.score > 10:
                return True
        return False

    def get_user_info(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user.name, user.email

    def get_transaction_history(self, user_id):
        transaction_history = []
        for transaction in self.transactions:
            if transaction.user_id == user_id:
                transaction_history.append((transaction.id, transaction.amount, transaction.type))
        return transaction_history

system = BankingFraudDetectionSystem()
system.add_user(1, 'John Doe', 'john.doe@example.com')
system.add_user(2, 'Jane Doe', 'jane.doe@example.com')
system.add_transaction(1, 1, 1500, 'withdrawal')
system.add_transaction(2, 1, 2000, 'deposit')
system.add_transaction(3, 2, 3000, 'withdrawal')
system.calculate_risk_score(1)
system.calculate_risk_score(2)
print(system.detect_fraud(1))
print(system.detect_fraud(2))
print(system.get_user_info(1))
print(system.get_transaction_history(1))