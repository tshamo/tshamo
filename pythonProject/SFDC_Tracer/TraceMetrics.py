class TraceMetrics:
    def __init__(self, metricName, seriesId, transactionId):
        self.seriesId = seriesId
        self.metricName = metricName
        self.seriesName = metricName
        self.transactionId = transactionId


metric_1 = TraceMetrics("root",0, 123455)

print(metric_1.seriesId)
print(metric_1.metricName)
print(metric_1.seriesName)
print(metric_1.transactionId)
