genetic-feature-selection
=========================


This package implements a genetic algorithm used for feature search.
--------------------------------------------------------------------

The genetic-feature-selection framework is used to search for a set for features that maximize some fitness function. It's made to be as easy as possible to use. 

The package implements heuristics based on the F-score, along side more stand genetic search. Use the F-score heuristic if you a faster search. 

.. note::

   Note that the package tries to maximize the fitness function. If you want to minimize, for example, MSE, you should multiply it by -1. The score will initialize to 
   negative infinity. 

Example of use
--------------

.. code:: python 

    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import average_precision_score
    from sklearn.model_selection import train_test_split
    from genetic_feature_selection.genetic_search import GeneticSearch
    from genetic_feature_selection.f_score_generator import FScoreSoftmaxInitPop
    import pandas as pd


    X, y = make_classification(n_samples=1000, n_informative=20, n_redundant=0)
    X = pd.DataFrame(X)
    y = pd.Series(y, name="y", dtype=int)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    X.columns = [f"col_{i}" for i in X.columns]


    gsf = GeneticSearch(
        # the search will do 5 iterations
        iterations = 5, 
        # each generation will have 4 possible solutions
        sol_per_pop = 4, 
        # every iteration will go through 15 generations 
        generations = 15, 
        # in each generation the 4 best individuals will be kept
        keep_n_best_individuals = 4, 
        # we want to find the 5 features that optimize average precision score
        select_n_features = 5,
        # 4 of the parents will be mating, this means the 4 best solutions in
        # each generation will be combined and create the basis for the next
        # generation
        num_parents_mating = 4,
        X_train = X_train,
        y_train = y_train,
        X_test = X_test,
        y_test = y_test,
        clf = LogisticRegression,
        clf_params = dict(max_iter=15),
        probas = True,
        scorer = average_precision_score,
        gen_pop = FScoreSoftmaxInitPop(
            X_train, y_train, tau = 50
        )
    )


    best_cols = gsf.search()


Example of use with f-score initialization and custom fitness function
----------------------------------------------------------------------

.. code:: python 

    .......

    class FitnessFunc:
        X_train, X_test, y_train, y_test = X_train, X_test, y_train, y_test
        clf_params = {}
        clf = LogisticRegression

        def __call__(self, soln): 
            X_train_soln = get_features(self.X_train, soln)
            X_val_son = get_features(self.X_test, soln)

            clf = self.clf(**self.clf_params)
            clf.fit(X_train_soln, self.y_train)

            preds = clf.predict_proba(X_val_son)[:,1]

            return average_precision_score(self.y_test, preds)


    fitness_func = FitnessFunc()

    gsf = GeneticSearch(
        iterations = 10, 
        sol_per_pop = 4, 
        generations = 15, 
        keep_n_best_individuals = 4, 
        select_n_features = 5,
        num_parents_mating = 4,
        X_train = X_train,
        y_train = y_train,
        X_test = X_test,
        y_test = y_test,
        gen_pop = FScoreSoftmaxInitPop(
            X_train, y_train, tau = 50
        ),
        fitness_func=fitness_func
    )

    gsf.search()



Example of custom fitness function where some features should be used regardless
--------------------------------------------------------------------------------

.. code:: python 

    .....
    keep_cols = ["col_0", "col_10"]
    X_train_keep_cols = X_train[keep_cols]
    X_train = X_train[[c for c in X_train.columns if c not in keep_cols]]
    X_test_keep_cols = X_test[keep_cols]
    X_test = X_test[[c for c in X_test.columns if c not in keep_cols]]

    logger = setup_logger(to_file=True)


    class FitnessFunc:
        def __init__(
            self, 
            X_train, y_train,
            X_test, y_test, 
            X_train_keep_cols,
            X_test_keep_cols,
        ) -> None:
            self.X_train, self.y_train = X_train, y_train
            self.X_test, self.y_test = X_test, y_test 
            self.X_train_keep_cols = X_train_keep_cols
            self.X_test_keep_cols = X_test_keep_cols
            self.clf_params = {} 
            self.clf = LogisticRegression 
            self.keep_cols = keep_cols 
            
        def __call__(self, soln): 
            X_train_soln = get_features(self.X_train, soln)
            X_val_son = get_features(self.X_test, soln)
            X_train_soln = pd.concat([X_train_soln, self.X_train_keep_cols], axis=1)
            X_val_son = pd.concat([X_val_son, self.X_test_keep_cols], axis=1)
            clf = self.clf(**self.clf_params)
            clf.fit(X_train_soln, self.y_train)
            preds = clf.predict_proba(X_val_son)[:,1]
            return average_precision_score(self.y_test, preds)
