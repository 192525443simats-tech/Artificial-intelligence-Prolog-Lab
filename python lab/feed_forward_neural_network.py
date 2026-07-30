from sklearn.neural_network import MLPClassifier

# Training data (XOR)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [0, 1, 1, 0]

# Create Feed Forward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='logistic',
    solver='adam',
    max_iter=5000,
    random_state=42
)

# Train the model
model.fit(X, y)

# Test data
test_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Predict
predictions = model.predict(test_data)

print("Feed Forward Neural Network Predictions:")
for i in range(len(test_data)):
    print(f"{test_data[i]} -> {predictions[i]}")