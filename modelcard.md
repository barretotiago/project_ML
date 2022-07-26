# Model Card 

A estruturação desse model card foi elaborado de acordo com a proposta de [Wu et al. (2019)](https://arxiv.org/pdf/1810.03993.pdf);

## *Model Details*: 
O projeto apresenta o uso de Machine Learning no treinamento de um modelo de classificação focado na avaliação de carros. 
O modelo foi retirado do Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Car+Evaluation) que é um sistema especialista 
para tomada de decisão e tem como objetivo avaliar carros de acordo com a aceitabilidade do carro, preço, características técnicas, conforto e segurança.
- Model date: Junho 1997.

## *Pipeline*:
O modelo de desenvolvimento de projeto seguiu a estrutura MLOPs proposta pelo prof. Dr. Ivanovitch Silva [https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/images/workflow.png]


![The Ivanovith's pipeline model.](../images/ivanovicth_workflow.png)

## *Intended Use*: 
Utilização de métodos de machine learning para desenvolvimento dos resultados. Foram utilizados aspectos de modelos já utilizados no repositório "my_first_action". A estruturação envolveu: Fecth data, EDA, Preprocessing, Data check, Data Segregation, Train and Test. A complementação do processo consistiu na utilização do [TensorFlow](https://www.tensorflow.org/), no processo de treinamento da rede. 

## *Complementary material*:
Para a construção do modelo, foram utilizados os seguintes materiais de opoio:
1)[TensorFlow uses] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_10/Notebooks/Week%2010%20Task%2001%20-%20TensorFlow%202.x%20%2B%20Keras%20Crash%20Course.ipynb);
2)[Better learning] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_10/Notebooks/Week%2010%20Task%2002%20-%20Better%20Learning%20part%20I.ipynb);
3)[Better learning II] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_12/Better%20Learning%20II.ipynb);
4)[Better learning III] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_12/Better%20Learning%20III.ipynb)
5) [Better Generalization] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_12/Better%20Generalization%20I.ipynb);
6) [Better Generalization II] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_12/Better%20Generalization%20II.ipynb);
7) [Hyperparameter tunning with keras] (https://github.com/ivanovitchm/ppgeecmachinelearning/blob/main/lessons/week_14/Task%20%2301%20Hyperparameter%20Tuning%20using%20Keras%20Tuner.ipynb);


## *Metrics*:
As principais métricas avaliadas nesse projeto são:

* [accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html);
* [f1](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score);
* [precision](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score); and
* [recall](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score).
