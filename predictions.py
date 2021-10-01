import keras
import numpy as np
import pandas as pd
import plotly
import tensorflow as tf
from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.preprocessing.sequence import TimeseriesGenerator

filename = 'powerball.csv'
df = pd.read_csv(filename)
print(df.info())


# change the drop columns order
df['date'] = pd.to_datetime(df['date'])
df.set_axis(df['date'], inplace=True)
df.drop(columns=['first', 'second', 'fourth', 'third', 'fifth'], inplace=True)

close_data = df['powerball'].values
close_data = close_data.reshape((-1,1))

split_percent = 0.80
split = int(split_percent*len(close_data))

close_train = close_data[:split]
close_test = close_data[split:]

date_train = df['date'][:split]
date_test = df['date'][split:]

print(len(close_train))
print(len(close_test))

look_back = 3

train_generator = TimeseriesGenerator(close_train, close_train, length=look_back, batch_size=20)     
test_generator = TimeseriesGenerator(close_test, close_test, length=look_back, batch_size=1)

model = Sequential()
model.add(
    LSTM(10,
        activation='relu',
        input_shape=(look_back,1))
)
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

num_epochs = 55
model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

prediction = model.predict(test_generator)

print(prediction)

close_train = close_train.reshape((-1))
close_test = close_test.reshape((-1))
prediction = prediction.reshape((-1))

print(prediction)

# trace1 = go.Scatter(
#     x = date_train,
#     y = close_train,
#     mode = 'lines',
#     name = 'Data'
# )
# trace2 = go.Scatter(
#     x = date_test,
#     y = prediction,
#     mode = 'lines',
#     name = 'Prediction'
# )
# trace3 = go.Scatter(
#     x = date_test,
#     y = close_test,
#     mode='lines',
#     name = 'Ground Truth'
# )
# layout = go.Layout(
#     title = "Google Stock",
#     xaxis = {'title' : "Date"},
#     yaxis = {'title' : "Close"}
# )
# fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
# fig.show()

# close_data = close_data.reshape((-1))

# def predict(num_prediction, model):
#     prediction_list = close_data[-look_back:]
#     for y in range(num_prediction):
# 		x = prediction_list[-look_back:]
# 		x = x.reshape((1, look_back, 1))
# 		out = model.predict(x)[0][0]
# 		prediction_list = np.append(prediction_list, out)
# 	prediction_list = prediction_list[look_back-1:]      
# 	return prediction_list
    
# def predict_dates(num_prediction):
#     last_date = df['Date'].values[-1]
#     prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
#     return prediction_dates

# num_prediction = 2
# forecast = predict(num_prediction, model)
# forecast_dates = predict_dates(num_prediction)
