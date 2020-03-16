library(keras)

library(ggplot2)
library(tidyr)
plot_training_losses <- function(losses) {
  loss_names <- names(losses)
  losses <- as.data.frame(losses)
  losses$epoch <- seq_len(nrow(losses))
  losses %>% 
    gather(model, loss, loss_names[[1]], loss_names[[2]]) %>% 
    ggplot(aes(x = epoch, y = loss, colour = model)) +
    geom_point()
}

imdb <- dataset_imdb(num_words = 10000)
c(c(train_data, train_labels), c(test_data, test_labels)) %<-% imdb

str(train_data[[1]])

train_labels[[1]]

max(sapply(train_data, max))

word_index <- dataset_imdb_word_index()
reverse_word_index <- names(word_index)
names(reverse_word_index) <- word_index

decoded_review <- sapply(train_data[[1]], function(index) {
  word <- if (index >= 3) reverse_word_index[[as.character(index - 3)]]
  if (!is.null(word)) word else "?"
})

cat(decoded_review)
                                                                                                                                                                            
vectorize_sequences <- function(sequences, dimension = 10000) {

results <- matrix(0, nrow = length(sequences), ncol = dimension)
for (i in 1:length(sequences))
    # Sets specific indices of results[i] to 1s
    results[i, sequences[[i]]] <- 1
    results
}

x_train <- vectorize_sequences(train_data)
x_test <- vectorize_sequences(test_data)

str(x_train[1,])

y_train <- as.numeric(train_labels)
y_test <- as.numeric(test_labels)

model <- keras_model_sequential()
layer_dense(units = 16, activation = "relu", input_shape = c(10000))
layer_dense(units = 16, activation = "relu")
layer_dense(units = 1, activation = "sigmoid")

val_indices <- 1:10000

x_val <- x_train[val_indices,]
partial_x_train <- x_train[-val_indices,]

y_val <- y_train[val_indices]
partial_y_train <- y_train[-val_indices]

model %>% compile(
    optimizer = "rmsprop",
    loss = "binary_crossentropy",
    metrics = c("accuracy")
)

history <- model %>% fit(
    partial_x_train,
    partial_y_train,
    epochs = 20,
    batch_size = 512,
    validation_data = list(x_val, y_val)
)

str(history)

plot(history)

model <- keras_model_sequential() %>% 
  layer_dense(units = 16, activation = "relu", input_shape = c(10000)) %>% 
  layer_dense(units = 16, activation = "relu") %>% 
  layer_dense(units = 1, activation = "sigmoid")

model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("accuracy")
)

model %>% compile(
      optimizer_rmsprop(lr=0.01),
      #optimizer = "rmsprop",
      loss = "binary_crossentropy",
      metrics = c("accuracy")
)

history <- model %>% fit(
  partial_x_train,
  partial_y_train,
  epochs = 20,
  batch_size = 512,
  validation_data = list(x_val, y_val)
)

results <- model %>% evaluate(x_test, y_test)

results

model %>% predict(x_test[1:10,])


#Regulaizer
model <- keras_model_sequential() %>% 
  layer_dense(units = 16, kernel_regularizer = regularizer_l2(0.001), activation = "relu", input_shape = c(10000)) %>% 
  layer_dense(units = 16, kernel_regularizer = regularizer_l2(0.001), activation = "relu") %>% 
  layer_dense(units = 1, activation = "sigmoid")


model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("accuracy")
)

original_hist <- model %>% fit(
  partial_x_train,
  partial_y_train,
  epochs = 20,
  batch_size = 512,
  validation_data = list(x_val, y_val)
)

dpt_model <- keras_model_sequential() %>% 
  layer_dense(units = 16, activation = "relu", input_shape = c(10000)) %>% 
  layer_dropout(rate = 0.5) %>% 
  layer_dense(units = 16, activation = "relu") %>% 
  layer_dropout(rate = 0.5) %>% 
  layer_dense(units = 1, activation = "sigmoid")
dpt_model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("acc")
)

dpt_model_hist <- dpt_model %>% fit(
  x_train, y_train,
  epochs = 20,
  batch_size = 512,
  validation_data = list(x_test, y_test)
)

plot_training_losses(losses = list(
  original_model = original_hist$metrics$val_loss,
  dpt_model = dpt_model_hist$metrics$val_loss
))
                                   