# No imports before this unzip!
try:
    import unzip_requirements
except ImportError:
    pass

from keras.models import load_model
import pandas as pd
import json


def endpoint(event: dict, context):
    try:
        model = load_model("./data/model.h5")
        input = []
        result_raw = model.predict(input)
        result = pd.DataFrame(result_raw)

        #         result.columns = ['home_team_score', 'away_team_score']
        #         scores_dictionary = result.iloc[0].round(0).astype('int').to_dict()

        body = {
            "message": result
        }

        response = {
            'statusCode': 200,
            'body': json.dumps(body)
        }
    except Exception as e:
        response = {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }

    return response
