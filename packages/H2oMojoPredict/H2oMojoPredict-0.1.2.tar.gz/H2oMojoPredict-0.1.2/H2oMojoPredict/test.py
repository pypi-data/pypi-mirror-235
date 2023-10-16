from H2oMojoPredict import H2oMojoPredictor
import pandas as pd
if __name__=='__main__':
    predictor = H2oMojoPredictor("XGBoost_model_python_1696751279647_2.zip", "binomial")
    data = pd.DataFrame({
        "os_act_first_diff": [55.0, 100.0],
        "life_cycle_string": ['4','3'],
    })
    java_service = predictor.start_java_service()
    result = predictor.predict_with_java_service(java_service, data)
    print(result)
    java_service.terminate()
    java_service.wait()
    if java_service.returncode == 0:
        print("Java service exited successfully.")
    else:
        print("Java service exited with an error code:", java_service.returncode)

