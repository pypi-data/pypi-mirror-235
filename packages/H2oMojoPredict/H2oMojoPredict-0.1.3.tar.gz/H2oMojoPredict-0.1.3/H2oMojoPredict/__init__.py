import sys

name = "H2oMojoPredict"

import subprocess
import json
import pandas as pd
import os

class H2oMojoPredictor(object):
    def __init__(self, model, _type="multivariate"):
        if _type not in ["multivariate", "regression", "ordinal", "binomial",
                         "autoencoder", "clustering", "dimreduction"]:
            raise NotImplementedError("Only 'multivariate', 'regression', 'ordinal', 'binomial', 'autoencoder', "
                                      "'clustering', and 'dimreduction' are supported predictor types")
        if not os.path.isfile(model):
            raise FileNotFoundError("Model file not found.")

        self.model = model
        self.type = _type


    def start_java_service(self):
        # 启动 Java JAR 服务并加载模型
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return subprocess.Popen(["java", "-jar", os.path.join(dir_path,"h2o_predict_java8.jar"), self.model, self.type],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)

    def predict_with_java_service(self, java_process, data):
        results_df = pd.DataFrame()

        # 将 Pandas 数据逐行发送到 Java JAR 服务的标准输入
        for _, row in data.iterrows():
            data_json = row.to_json()
            java_process.stdin.write(data_json + '\n')
            java_process.stdin.flush()

        java_process.stdin.close()

        # 从 Java JAR 服务的标准输出逐行读取预测结果
        for line in java_process.stdout:
            result = json.loads(line)

            # 处理每行预测结果并将其添加到 DataFrame
            row_df = pd.DataFrame([result])
            results_df = results_df.append(row_df, ignore_index=True)

        return results_df

    @staticmethod
    def supported_predictors():
        return ["multivariate", "regression", "ordinal", "binomial", "autoencoder", "clustering", "dimreduction"]
