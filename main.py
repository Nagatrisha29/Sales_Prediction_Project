from src.load_data import load_dataset
from src.preprocessing import split_data
from src.visualization import show_heatmap, show_pairplot
from src.model import train_model
from src.evaluation import evaluate
from src.predict import predict_new

# Load dataset
data = load_dataset("data/sales_data.csv")

# Visualization
show_heatmap(data)
show_pairplot(data)

# Preprocessing
X, y = split_data(data)

# Training
model, X_test, y_test = train_model(X, y)

# Evaluation
evaluate(model, X_test, y_test)

# Prediction
predict_new(model)