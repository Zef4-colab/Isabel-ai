import joblib

# Load the trained model
model = joblib.load('path_to_your_model/model.joblib')

# Function to make predictions

def make_prediction(user_input):
    prediction = model.predict([user_input])
    return prediction

# Example usage
def main():
    user_input = input('Enter your input: ')
    prediction = make_prediction(user_input)
    print('Prediction:', prediction)

if __name__ == '__main__':
    main()