# import packages and custom feature
# for building our models
from feature_engine.encoding import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

from classification_model.config.core import config

# set up the pipeline
customer_churn_pipeline = Pipeline(
    [
        # == CATEGORICAL ENCODING ======
        (
            "ordinal_encoder",
            OrdinalEncoder(variables=config.model_config.features),
        ),
        # ==== SCALING OUR data ========
        (
            "scaler",
            StandardScaler(),
        ),
        # final estimator
        (
            "xgb",
            XGBClassifier(
                eta=config.model_config.eta,
                alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
