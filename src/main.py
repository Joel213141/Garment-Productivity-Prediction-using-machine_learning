{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4958679b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import preprocessing\n",
    "import models\n",
    "import evaluation\n",
    "\n",
    "def main():\n",
    "    df = preprocessing.load_data(\"path_to_dataset.csv\")\n",
    "    X, y, label_encoders, scaler = preprocessing.preprocess_data(df)\n",
    "    X_train, X_test, y_train, y_test = preprocessing.split_data(X, y)\n",
    "    \n",
    "    # Train models\n",
    "    elastic_net_model = models.train_elastic_net(X_train, y_train)\n",
    "    svr_model = models.train_svr(X_train, y_train)\n",
    "    rf_model = models.train_random_forest(X_train, y_train)\n",
    "    \n",
    "    # Evaluate models\n",
    "    print(\"ElasticNet Performance:\", evaluation.evaluate_model(elastic_net_model, X_test, y_test))\n",
    "    print(\"SVR Performance:\", evaluation.evaluate_model(svr_model, X_test, y_test))\n",
    "    print(\"Random Forest Performance:\", evaluation.evaluate_model(rf_model, X_test, y_test))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
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
