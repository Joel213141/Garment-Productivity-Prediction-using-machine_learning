{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4958679b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler, LabelEncoder\n",
    "\n",
    "def load_data(filepath):\n",
    "    df = pd.read_csv(filepath)\n",
    "    return df\n",
    "\n",
    "def preprocess_data(df):\n",
    "    # Handling missing values\n",
    "    df = df.fillna(df.mean())\n",
    "    # Label encoding\n",
    "    label_encoders = {}\n",
    "    for column in ['date', 'quarter', 'department', 'day']:\n",
    "        le = LabelEncoder()\n",
    "        df[column] = le.fit_transform(df[column])\n",
    "        label_encoders[column] = le\n",
    "    # Feature scaling\n",
    "    scaler = StandardScaler()\n",
    "    scaled_features = scaler.fit_transform(df.drop('actual_productivity', axis=1))\n",
    "    return scaled_features, df['actual_productivity'], label_encoders, scaler\n",
    "\n",
    "def split_data(X, y, test_size=0.33, random_state=42):\n",
    "    from sklearn.model_selection import train_test_split\n",
    "    return train_test_split(X, y, test_size=test_size, random_state=random_state)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
