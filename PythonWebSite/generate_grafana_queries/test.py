{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "limit": 100,
        "name": "Annotations & Alerts",
        "showIn": 0,
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "description": "Summary",
  "editable": true,
  "gnetId": null,
  "graphTooltip": 0,
  "id": 13117,
  "iteration": 1657037867326,
  "links": [
    {
      "asDropdown": false,
      "icon": "external link",
      "includeVars": false,
      "keepTime": false,
      "tags": [
        "PRE_PROD",
        "Serice Cloud",
        "cuj"
      ],
      "targetBlank": true,
      "title": "New link",
      "tooltip": "",
      "type": "dashboards",
      "url": ""
    }
  ],
  "panels": [
    {
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 15,
        "x": 0,
        "y": 0
      },
      "id": 366,
      "options": {
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "8.1.8",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "default",
          "rawSql": "",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Cloud / Region",
      "type": "text"
    },
    {
      "datasource": null,
      "gridPos": {
        "h": 6,
        "w": 3,
        "x": 21,
        "y": 0
      },
      "id": 567,
      "options": {
        "content": "<center><p style=\"background-color:#6C310A;\">PRE_PROD</p>",
        "mode": "markdown"
      },
      "pluginVersion": "8.1.8",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "default",
          "rawSql": "",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Notes",
      "type": "text"
    },
    {
      "datasource": null,
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 0,
        "y": 1
      },
      "id": 538,
      "links": [],
      "options": {
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "8.1.8",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "default",
          "rawSql": "",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Service Cloud",
      "type": "text"
    },
    {
      "datasource": "argus",
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 3,
          "links": [
            {
              "targetBlank": true,
              "title": "drill down to Cloud",
              "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/72O_0DQ7z/cuj-service-cloud-dc-pod-pre_prod?from=${__from}&to=${__to}&var-Region=AMER"
            }
          ],
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "transparent",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "red",
                "value": 99.9
              },
              {
                "color": "yellow",
                "value": 99.94
              },
              {
                "color": "green",
                "value": 99.95
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 3,
        "y": 1
      },
      "id": 588,
      "libraryPanel": {
        "description": "",
        "meta": {
          "connectedDashboards": 2,
          "created": "2022-04-28T19:11:23Z",
          "createdBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          },
          "folderName": "1P SRE",
          "folderUid": "9r8PpnQZk",
          "updated": "2022-06-28T23:42:35Z",
          "updatedBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          }
        },
        "name": "AMER Service pre-prod",
        "type": "stat",
        "uid": "p7X-JXQnz",
        "version": 13
      },
      "links": [],
      "maxPerRow": 6,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "8.1.8",
      "repeatDirection": "h",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "hide": false,
          "queryMode": "expression",
          "rawSql": "AVERAGE(\n\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  ),\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  )\n  \n\n\n  \n)",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "AMER Service pre-prod",
      "type": "stat"
    },
    {
      "datasource": "argus",
      "description": "",
      "fieldConfig": {
        "defaults": {
          "decimals": 3,
          "links": [
            {
              "targetBlank": true,
              "title": "drill down to Cloud",
              "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/72O_0DQ7z/cuj-service-cloud-dc-pod-pre_prod?from=${__from}&to=${__to}&var-Region=EMEA"
            }
          ],
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "transparent",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "red",
                "value": 99.9
              },
              {
                "color": "yellow",
                "value": 99.94
              },
              {
                "color": "green",
                "value": 99.95
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 5,
        "y": 1
      },
      "id": 590,
      "libraryPanel": {
        "description": "",
        "meta": {
          "connectedDashboards": 2,
          "created": "2022-04-28T19:11:27Z",
          "createdBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          },
          "folderName": "1P SRE",
          "folderUid": "9r8PpnQZk",
          "updated": "2022-06-28T22:56:48Z",
          "updatedBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          }
        },
        "name": "EMEA Service pre-prod",
        "type": "stat",
        "uid": "l4e-1uQnk",
        "version": 12
      },
      "links": [],
      "maxPerRow": 6,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "8.1.8",
      "repeatDirection": "h",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "expression",
          "rawSql": "AVERAGE(\n\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  ),\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  )\n  \n\n  \n  \n)",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "EMEA Service pre-prod",
      "type": "stat"
    },
    {
      "datasource": "argus",
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 3,
          "links": [
            {
              "targetBlank": true,
              "title": "drill down to Cloud",
              "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/72O_0DQ7z/cuj-service-cloud-dc-pod-pre_prod?from=${__from}&to=${__to}&var-Region=APAC"
            }
          ],
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "transparent",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "red",
                "value": 99.9
              },
              {
                "color": "yellow",
                "value": 99.94
              },
              {
                "color": "green",
                "value": 99.95
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 7,
        "y": 1
      },
      "id": 592,
      "libraryPanel": {
        "description": "",
        "meta": {
          "connectedDashboards": 2,
          "created": "2022-04-28T19:11:31Z",
          "createdBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          },
          "folderName": "1P SRE",
          "folderUid": "9r8PpnQZk",
          "updated": "2022-06-28T22:57:20Z",
          "updatedBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          }
        },
        "name": "APAC Service pre-prod",
        "type": "stat",
        "uid": "OGZBJXw7k",
        "version": 8
      },
      "links": [],
      "maxPerRow": 6,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "8.1.8",
      "repeatDirection": "h",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "expression",
          "rawSql": "AVERAGE(\n\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,location=*,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,location=*,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  ),\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  )\n  \n\n  \n  \n)",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "APAC Service pre-prod",
      "type": "stat"
    },
    {
      "datasource": "argus",
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 3,
          "links": [
            {
              "targetBlank": true,
              "title": "drill down to cloud",
              "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/72O_0DQ7z/cuj-service-cloud-dc-pod-pre_prod?from=${__from}&to=${__to}"
            }
          ],
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "transparent",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "red",
                "value": 99.9
              },
              {
                "color": "yellow",
                "value": 99.94
              },
              {
                "color": "green",
                "value": 99.95
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 9,
        "y": 1
      },
      "id": 596,
      "libraryPanel": {
        "description": "",
        "meta": {
          "connectedDashboards": 2,
          "created": "2022-04-28T19:09:36Z",
          "createdBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          },
          "folderName": "1P SRE",
          "folderUid": "9r8PpnQZk",
          "updated": "2022-06-28T22:57:48Z",
          "updatedBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          }
        },
        "name": "Sandbox Service pre-prod",
        "type": "stat",
        "uid": "0sxAJuQnz",
        "version": 17
      },
      "links": [],
      "maxPerRow": 6,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "8.1.8",
      "repeatDirection": "h",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "expression",
          "rawSql": "AVERAGE(\n\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),\n                 \n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(INCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),\n                \n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  ),\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),\n                 \n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(INCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),\n                \n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  )\n\n  \n  \n)",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Sandbox Service pre-prod",
      "type": "stat"
    },
    {
      "datasource": "argus",
      "description": "",
      "fieldConfig": {
        "defaults": {
          "decimals": 3,
          "links": [
            {
              "targetBlank": true,
              "title": "drill down to Cloud",
              "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/72O_0DQ7z/cuj-service-cloud-dc-pod-pre_prod?from=${__from}&to=${__to}"
            }
          ],
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "transparent",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "red",
                "value": 99.9
              },
              {
                "color": "yellow",
                "value": 99.94
              },
              {
                "color": "green",
                "value": 99.95
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 11,
        "y": 1
      },
      "id": 594,
      "libraryPanel": {
        "description": "",
        "meta": {
          "connectedDashboards": 2,
          "created": "2022-04-28T19:09:16Z",
          "createdBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          },
          "folderName": "1P SRE",
          "folderUid": "9r8PpnQZk",
          "updated": "2022-06-28T22:58:30Z",
          "updatedBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          }
        },
        "name": "Hyperforce Service pre-prod",
        "type": "stat",
        "uid": "qceT1uwnk",
        "version": 21
      },
      "links": [],
      "maxPerRow": 6,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "8.1.8",
      "repeatDirection": "h",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "expression",
          "rawSql": "AVERAGE(\n\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELISTHF.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELISTHF.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  ),\n  \n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELISTHF.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELISTHF.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  )\n\n)",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Hyperforce Service pre-prod",
      "type": "stat"
    },
    {
      "datasource": "argus",
      "description": "",
      "fieldConfig": {
        "defaults": {
          "decimals": 3,
          "links": [
            {
              "targetBlank": true,
              "title": "drill down to Cloud",
              "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/72O_0DQ7z/cuj-service-cloud-dc-pod-pre_prod?from=${__from}&to=${__to}"
            }
          ],
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "transparent",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "red",
                "value": 99.9
              },
              {
                "color": "yellow",
                "value": 99.94
              },
              {
                "color": "green",
                "value": 99.95
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 13,
        "y": 1
      },
      "id": 624,
      "libraryPanel": {
        "description": "",
        "meta": {
          "connectedDashboards": 2,
          "created": "2022-06-23T15:38:50Z",
          "createdBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          },
          "folderName": "1P SRE",
          "folderUid": "9r8PpnQZk",
          "updated": "2022-06-28T22:59:44Z",
          "updatedBy": {
            "avatarUrl": "/avatar/cb92f76cc8f84188810d8370ad741862",
            "id": 363,
            "name": "taulant.shamo"
          }
        },
        "name": "Hyperforce SB - Service pre-prod",
        "type": "stat",
        "uid": "POCPKK3nz",
        "version": 2
      },
      "links": [],
      "maxPerRow": 6,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "8.1.8",
      "repeatDirection": "h",
      "targets": [
        {
          "aggregator": "avg",
          "downsampleAggregator": "avg",
          "queryMode": "expression",
          "rawSql": "AVERAGE(\n\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(INCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  ),\n  DOWNSAMPLE(\n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(INCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    #all-avg#\n  )\n\n)",
          "refId": "A",
          "target": "select metric",
          "type": "timeserie"
        }
      ],
      "timeFrom": null,
      "timeShift": null,
      "title": "Hyperforce SB - Service pre-prod",
      "type": "stat"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 6
      },
      "id": 608,
      "panels": [
        {
          "datasource": null,
          "gridPos": {
            "h": 3,
            "w": 3,
            "x": 0,
            "y": 7
          },
          "id": 609,
          "links": [],
          "options": {
            "content": "<center><br><a href=\"https://kaiju.data.sfdc.net/synthetics/api/testcases/33101\" target=\"_blank\">33101</a><br>CUJ - CRM - Post update to case</center>",
            "mode": "markdown"
          },
          "pluginVersion": "8.1.8",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "default",
              "rawSql": "",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "type": "text"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 3,
            "y": 7
          },
          "id": 610,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$AMER,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),#10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$AMER,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),#10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "AMER",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 5,
            "y": 7
          },
          "id": 611,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$EMEA,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),#10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$EMEA,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),#10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "EMEA",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 7,
            "y": 7
          },
          "id": 612,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$APAC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),#10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$APAC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),#10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "APAC",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 9,
            "y": 7
          },
          "id": 613,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(INCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$ALLDC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),#10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(INCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=$ALLDC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),#10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Sandbox",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 11,
            "y": 7
          },
          "id": 614,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=$EXCLUDELISTHF.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=$EXCLUDELISTHF.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 13,
            "y": 7
          },
          "id": 615,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(INCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(INCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{location=*,level=testCase,testCaseId=33101,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce Sandbox",
          "type": "stat"
        },
        {
          "datasource": null,
          "gridPos": {
            "h": 3,
            "w": 3,
            "x": 0,
            "y": 10
          },
          "id": 617,
          "links": [],
          "options": {
            "content": "<center><br><a href=\"https://kaiju.data.sfdc.net/synthetics/api/testcases/32062\" target=\"_blank\">32062</a><br>CUJ - CRM - All - Edit case</center>",
            "mode": "markdown"
          },
          "pluginVersion": "8.1.8",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "default",
              "rawSql": "",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "type": "text"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 3,
            "y": 10
          },
          "id": 616,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$AMER,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$AMER,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "AMER",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 5,
            "y": 10
          },
          "id": 618,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$EMEA,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$EMEA,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "EMEA",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 7,
            "y": 10
          },
          "id": 619,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$APAC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$APAC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=$EXCLUDELIST.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "APAC",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 9,
            "y": 10
          },
          "id": 620,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(INCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$ALLDC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(INCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=$ALLDC,operationalStatus=ACTIVE,podName=*,substrate=SFDC_CORE}:max:10m-max,\n#(.*podName=cs.*)#),#(.*podName=$EXCLUDELISTSB.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Sandbox",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 11,
            "y": 10
          },
          "id": 621,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=$EXCLUDELISTHF.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=$EXCLUDELISTHF.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 2,
            "x": 13,
            "y": 10
          },
          "id": 622,
          "links": [],
          "maxPerRow": 6,
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "AVERAGE(\nDOWNSAMPLE(    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      PROPAGATE(\nEXCLUDE(INCLUDE(                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#),                        #10m#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    PROPAGATE(\nEXCLUDE(INCLUDE(                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{location=*,level=testCase,testCaseId=32062,dataCenterName=*,podName=*,substrate=AWS}:max:10m-max,\n#(.*podName=.*s,.*)#),#(.*podName=$EXCLUDELISTHFSB.*)#),                      #10m#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #dataCenterName#,#AVERAGE#\n      ),\n      #100#\n    )\n,#all-avg#)\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce Sandbox",
          "type": "stat"
        }
      ],
      "title": "By Test",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 7
      },
      "id": 487,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 13,
            "x": 0,
            "y": 8
          },
          "id": 581,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "value_and_name"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n  \n    DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELIST.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    ),\n        DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELIST.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    )\n\n    \n    \n    ,\n    #dataCenterName#,#AVERAGE#\n  ),\n  #dataCenterName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "AMER Datacenters",
          "transformations": [
            {
              "id": "filterFieldsByName",
              "options": {
                "include": {
                  "names": [
                    "Time",
                    "DFW",
                    "IA2",
                    "IA4",
                    "IA5",
                    "PH2",
                    "PHX",
                    "YHU",
                    "YUL"
                  ]
                }
              }
            }
          ],
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/ffEysDQ7k/cuj-service-cloud-pod-cujs-wip-pre_prod?orgId=1&var-pod=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 13,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 582,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n        SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$AMER,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n\n    \n    \n    #podName#,#AVERAGE#\n  ),\n  #podName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "AMER Pods",
          "type": "stat"
        }
      ],
      "title": "AMER",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 8
      },
      "id": 576,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 7,
            "x": 0,
            "y": 9
          },
          "id": 508,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "vertical",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n  \n    DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELIST.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    ),\n        DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELIST.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    )\n    \n    \n    ,\n    #dataCenterName#,#AVERAGE#\n  ),\n  #dataCenterName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "EMEA Datacenters",
          "transformations": [
            {
              "id": "filterFieldsByName",
              "options": {
                "include": {
                  "names": [
                    "Time",
                    "CDG",
                    "FRA",
                    "LO2",
                    "LO3"
                  ]
                }
              }
            }
          ],
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/ffEysDQ7k/cuj-service-cloud-pod-cujs-wip-pre_prod?orgId=1&var-pod=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 13
          },
          "id": 511,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "hide": false,
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n        SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$EMEA,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n\n    \n    \n    #podName#,#AVERAGE#\n  ),\n  #podName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "EMEA Pods",
          "type": "stat"
        }
      ],
      "title": "EMEA",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 9
      },
      "id": 574,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 6,
            "x": 0,
            "y": 10
          },
          "id": 507,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "vertical",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n  \n    DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELIST.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    ),\n        DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELIST.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    )\n\n    \n    \n    ,\n    #dataCenterName#,#AVERAGE#\n  ),\n  #dataCenterName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "APAC Datacenters",
          "transformations": [
            {
              "id": "filterFieldsByName",
              "options": {
                "include": {
                  "names": [
                    "Time",
                    "HND",
                    "SYD",
                    "UKB"
                  ]
                }
              }
            }
          ],
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/ffEysDQ7k/cuj-service-cloud-pod-cujs-wip-pre_prod?orgId=1&var-pod=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 14
          },
          "id": 512,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n        SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELIST.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$APAC,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELIST.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n\n    \n    \n    #podName#,#AVERAGE#\n  ),\n  #podName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "APAC Pods",
          "type": "stat"
        }
      ],
      "title": "APAC",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 10
      },
      "id": 578,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 24,
            "x": 0,
            "y": 11
          },
          "id": 534,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "vertical",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          INCLUDE(\n                            PROPAGATE(\n                              $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                            ),\n                            #(.*podName=cs.*)#\n                          ),\n                          #(.*podName=$EXCLUDELISTSB.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,podName=*,dataCenterName=$ALLDC,substrate=SFDC_CORE,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=cs.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTSB.*)#\n                      ),\n                      #podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    ),\n      DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          INCLUDE(\n                            PROPAGATE(\n                              $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                            ),\n                            #(.*podName=cs.*)#\n                          ),\n                          #(.*podName=$EXCLUDELISTSB.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,podName=*,dataCenterName=$ALLDC,substrate=SFDC_CORE,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=cs.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTSB.*)#\n                      ),\n                      #podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    )\n\n    \n    \n    ,\n    #dataCenterName#,#AVERAGE#\n  ),\n  #dataCenterName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Sandbox Datacenters",
          "transformations": [
            {
              "id": "filterFieldsByName",
              "options": {
                "include": {
                  "names": [
                    "Time",
                    "CDG",
                    "DFW",
                    "FRA",
                    "HND",
                    "IA2",
                    "IA4",
                    "IA5",
                    "LO2",
                    "LO3",
                    "ORD",
                    "PH2",
                    "PHX",
                    "SYD",
                    "UKB",
                    "YHU",
                    "YUL"
                  ]
                }
              }
            }
          ],
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/ffEysDQ7k/cuj-service-cloud-pod-cujs-wip-pre_prod?orgId=1&var-pod=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 18,
            "w": 24,
            "x": 0,
            "y": 15
          },
          "id": 510,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=cs.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTSB.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=cs.*)#\n                      ),\n                      #(.*podName=$EXCLUDELISTSB.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    \n        SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=cs.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTSB.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{operationalStatus=ACTIVE,dataCenterName=$ALLDC,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=cs.*)#\n                      ),\n                      #(.*podName=$EXCLUDELISTSB.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    \n\n\n    #podName#,#AVERAGE#\n  ),\n  #podName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Sandbox Pods",
          "type": "stat"
        }
      ],
      "title": "Sandbox",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 11
      },
      "id": 572,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "decimals": 3,
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 569,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELISTHF.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELISTHF.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    ),\n        DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=$EXCLUDELISTHF.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELISTHF.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    )\n    \n\n    \n    \n    ,\n    #dataCenterName#,#AVERAGE#\n  ),\n  #dataCenterName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/yxqp11unk/cuj-service-cloud-pod-cujs-hyperforce-wip-pre_prod?orgId=1&var-instance=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 20,
            "w": 24,
            "x": 0,
            "y": 16
          },
          "id": 570,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELISTHF.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELISTHF.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    \n        SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=$EXCLUDELISTHF.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      PROPAGATE(\n                        $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                      ),\n                      #(.*podName=$EXCLUDELISTHF.*)#\n                    ),\n                    #podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    \n\n    \n    #podName#,#AVERAGE#\n  ),\n  #podName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce Cells",
          "type": "stat"
        }
      ],
      "title": "Hyperforce",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 12
      },
      "id": 604,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 24,
            "x": 0,
            "y": 13
          },
          "id": 605,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          INCLUDE(\n                            PROPAGATE(\n                              $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                            ),\n                            #(.*podName=.*s,.*)#\n                          ),\n                          #(.*podName=$EXCLUDELISTHFSB.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=.*s,.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTHFSB.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    ),\n        DOWNSAMPLE(\n      SCALE(\n        GROUPBYTAG(\n          FILL(\n            GROUPBYTAG(\n              CULL_BELOW(\n                FILL(\n                  GROUPBYTAG(\n                    GROUPBYTAG(\n                      CULL_BELOW(\n                        EXCLUDE(\n                          INCLUDE(\n                            PROPAGATE(\n                              $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                            ),\n                            #(.*podName=.*s,.*)#\n                          ),\n                          #(.*podName=$EXCLUDELISTHFSB.*)#\n                        ),\n                        #-0.5#,#value#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    GROUPBYTAG(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=.*s,.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTHFSB.*)#\n                      ),\n                      #testCaseId#,#podName#,#COUNT#\n                    ),\n                    #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                  ),\n                  #10m#,#0m#,#1#\n                ),\n                #0.01#,#value#\n              ),\n              #testCaseId#,#podName#,#COUNT#\n            ),\n            #10m#,#0m#,#0#\n          ),\n          #dataCenterName#,#AVERAGE#\n        ),\n        #100#\n      ),\n      #all-avg#\n    )\n\n    \n    ,\n    #dataCenterName#,#AVERAGE#\n  ),\n  #dataCenterName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce Sandbox",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/yxqp11unk/cuj-service-cloud-pod-cujs-hyperforce-wip-pre_prod?orgId=1&var-instance=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 24,
            "x": 0,
            "y": 17
          },
          "id": 606,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(\n  GROUPBYTAG(\n  \n    SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=.*s,.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTHFSB.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=.*s,.*)#\n                      ),\n                      #(.*podName=$EXCLUDELISTHFSB.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n        SCALE(\n      GROUPBYTAG(\n        FILL(\n          GROUPBYTAG(\n            CULL_BELOW(\n              FILL(\n                GROUPBYTAG(\n                  GROUPBYTAG(\n                    CULL_BELOW(\n                      EXCLUDE(\n                        INCLUDE(\n                          PROPAGATE(\n                            $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                          ),\n                          #(.*podName=.*s,.*)#\n                        ),\n                        #(.*podName=$EXCLUDELISTHFSB.*)#\n                      ),\n                      #-0.5#,#value#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  GROUPBYTAG(\n                    EXCLUDE(\n                      INCLUDE(\n                        PROPAGATE(\n                          $start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__Post__update__to__case_availability{dataCenterName=*,substrate=AWS,podName=*,level=testCase,testCaseId=33101}:max:10m-max,#10m#\n                        ),\n                        #(.*podName=.*s,.*)#\n                      ),\n                      #(.*podName=$EXCLUDELISTHFSB.*)#\n                    ),\n                    #testCaseId#,#podName#,#COUNT#\n                  ),\n                  #testCaseId#,#podName#,#DIVIDE#,#UNION#,#0#\n                ),\n                #10m#,#0m#,#1#\n              ),\n              #0.01#,#value#\n            ),\n            #testCaseId#,#podName#,#COUNT#\n          ),\n          #10m#,#0m#,#0#\n        ),\n        #testCaseId#,#podName#,#AVERAGE#\n      ),\n      #100#\n    ),\n    \n    \n\n    \n    \n    #podName#,#AVERAGE#\n  ),\n  #podName#\n)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Hyperforce Sandbox Cells",
          "type": "stat"
        }
      ],
      "title": "Hyperforce SB",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": null,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 13
      },
      "id": 598,
      "panels": [
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 13,
            "x": 0,
            "y": 13
          },
          "id": 600,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(SCALE( GROUPBYTAG( FILL(\n    GROUPBYTAG(\n      CULL_BELOW(\n        FILL(\n          GROUPBYTAG(\n            GROUPBYTAG(\n              CULL_BELOW(EXCLUDE(\n                PROPAGATE($start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$Region,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#),#(.*podName=$EXCLUDELISTALL.*)#),#-0.5#,#value#\n              ),\n              #podName#,#dataCenterName#,#COUNT#\n            ),\n            GROUPBYTAG(EXCLUDE(\n              PROPAGATE($start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$Region,substrate=SFDC_CORE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#),#(.*podName=$EXCLUDELISTALL.*)#),#podName#,#COUNT#\n            ),\n            #podName#,#dataCenterName#,#DIVIDE#,#UNION#,#0#\n          ),\n          #10m#,#0m#,#1#\n        ),\n        #0.01#,#value#\n      ),\n      #podName#,#dataCenterName#,#COUNT#\n    ),\n    #10m#,#0m#,#0#\n  ), #dataCenterName#,#AVERAGE#)\n, #100#), #dataCenterName#)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "$Region Datacenters",
          "type": "stat"
        },
        {
          "datasource": "argus",
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [
                {
                  "targetBlank": true,
                  "title": "drill down to ${__series.name}",
                  "url": "https://grafana.argus.monitoring.aws-esvc1-useast2.aws.sfdc.cl/d/ffEysDQ7k/cuj-service-cloud-pod-cujs-wip-pre_prod?orgId=1&var-pod=${__series.name}&from=${__from}&to=${__to}"
                }
              ],
              "mappings": [
                {
                  "options": {
                    "match": "null",
                    "result": {
                      "color": "transparent",
                      "index": 0
                    }
                  },
                  "type": "special"
                }
              ],
              "max": 100,
              "min": 0,
              "thresholds": {
                "mode": "percentage",
                "steps": [
                  {
                    "color": "red",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 99.9
                  },
                  {
                    "color": "yellow",
                    "value": 99.94
                  },
                  {
                    "color": "green",
                    "value": 99.95
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 13,
            "w": 24,
            "x": 0,
            "y": 17
          },
          "id": 601,
          "links": [],
          "options": {
            "colorMode": "background",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "mean"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.1.8",
          "repeatDirection": "h",
          "targets": [
            {
              "aggregator": "avg",
              "downsampleAggregator": "avg",
              "queryMode": "expression",
              "rawSql": "ALIASBYTAG(SCALE(  FILL(\n    GROUPBYTAG(\n      CULL_BELOW(\n        FILL(\n          GROUPBYTAG(\n            GROUPBYTAG(\n              CULL_BELOW(EXCLUDE(\n                PROPAGATE($start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$Region,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#),#(.*podName=$EXCLUDELISTALL.*)#),#-0.5#,#value#\n              ),\n              #podName#,#COUNT#\n            ),\n            GROUPBYTAG(EXCLUDE(\n              PROPAGATE($start:$end:synthetics.*.AGG.all:kaiju_CUJ__-__CRM__-__All__-__Edit__case_availability{operationalStatus=ACTIVE,dataCenterName=$Region,substrate=SFDC_CORE,operationalStatus=ACTIVE,podName=*,level=testCase,testCaseId=32062}:max:10m-max,#10m#),#(.*podName=$EXCLUDELISTALL.*)#),#podName#,#COUNT#\n            ),\n            #podName#,#DIVIDE#,#UNION#,#0#\n          ),\n          #10m#,#0m#,#1#\n        ),\n        #0.01#,#value#\n      ),\n      #podName#,#COUNT#\n    ),\n    #10m#,#0m#,#0#\n  )\n, #100#),#podName#)",
              "refId": "A",
              "target": "select metric",
              "type": "timeserie"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "$Region Pods",
          "type": "stat"
        }
      ],
      "repeat": "Region",
      "title": "$Region - Auto - WIP",
      "type": "row"
    }
  ],
  "refresh": false,
  "schemaVersion": 30,
  "style": "dark",
  "tags": [
    "PRE_PROD",
    "Service Cloud",
    "cuj"
  ],
  "templating": {
    "list": [
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": [
            "Service_Cloud"
          ],
          "value": [
            "Service_Cloud"
          ]
        },
        "description": null,
        "error": null,
        "hide": 2,
        "includeAll": true,
        "label": "Service Cloud",
        "multi": true,
        "name": "ServiceCloud",
        "options": [
          {
            "selected": false,
            "text": "All",
            "value": "$__all"
          },
          {
            "selected": false,
            "text": "Sales_Cloud",
            "value": "Sales_Cloud"
          },
          {
            "selected": true,
            "text": "Service_Cloud",
            "value": "Service_Cloud"
          },
          {
            "selected": false,
            "text": "Platform",
            "value": "Platform"
          },
          {
            "selected": false,
            "text": "Marketing",
            "value": "Marketing"
          }
        ],
        "query": "Sales_Cloud,Service_Cloud,Platform,Marketing",
        "queryValue": "",
        "skipUrlSync": false,
        "type": "custom"
      },
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": "HND|SYD|UKB",
          "value": "HND|SYD|UKB"
        },
        "description": null,
        "error": null,
        "hide": 2,
        "includeAll": false,
        "label": null,
        "multi": false,
        "name": "APAC",
        "options": [
          {
            "selected": true,
            "text": "HND|SYD|UKB",
            "value": "HND|SYD|UKB"
          }
        ],
        "query": "HND|SYD|UKB",
        "queryValue": "",
        "skipUrlSync": false,
        "type": "custom"
      },
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": "IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL",
          "value": "IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL"
        },
        "description": null,
        "error": null,
        "hide": 2,
        "includeAll": false,
        "label": null,
        "multi": false,
        "name": "AMER",
        "options": [
          {
            "selected": true,
            "text": "IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL",
            "value": "IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL"
          }
        ],
        "query": "IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL",
        "skipUrlSync": false,
        "type": "custom"
      },
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": "CDG|LO2|LO3|FRA",
          "value": "CDG|LO2|LO3|FRA"
        },
        "description": null,
        "error": null,
        "hide": 2,
        "includeAll": false,
        "label": null,
        "multi": false,
        "name": "EMEA",
        "options": [
          {
            "selected": true,
            "text": "CDG|LO2|LO3|FRA",
            "value": "CDG|LO2|LO3|FRA"
          }
        ],
        "query": "CDG|LO2|LO3|FRA",
        "skipUrlSync": false,
        "type": "custom"
      },
      {
        "auto": false,
        "auto_count": 30,
        "auto_min": "10s",
        "current": {
          "selected": false,
          "text": "5m",
          "value": "5m"
        },
        "description": null,
        "error": null,
        "hide": 0,
        "label": "Downsampling",
        "name": "downInterval",
        "options": [
          {
            "selected": false,
            "text": "1m",
            "value": "1m"
          },
          {
            "selected": false,
            "text": "2m",
            "value": "2m"
          },
          {
            "selected": true,
            "text": "5m",
            "value": "5m"
          },
          {
            "selected": false,
            "text": "10m",
            "value": "10m"
          },
          {
            "selected": false,
            "text": "30m",
            "value": "30m"
          },
          {
            "selected": false,
            "text": "1h",
            "value": "1h"
          },
          {
            "selected": false,
            "text": "6h",
            "value": "6h"
          },
          {
            "selected": false,
            "text": "12h",
            "value": "12h"
          },
          {
            "selected": false,
            "text": "1d",
            "value": "1d"
          },
          {
            "selected": false,
            "text": "7d",
            "value": "7d"
          },
          {
            "selected": false,
            "text": "14d",
            "value": "14d"
          },
          {
            "selected": false,
            "text": "30d",
            "value": "30d"
          }
        ],
        "query": "1m,2m,5m,10m,30m,1h,6h,12h,1d,7d,14d,30d",
        "queryValue": "",
        "refresh": 2,
        "skipUrlSync": false,
        "type": "interval"
      },
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": "HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA",
          "value": "HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA"
        },
        "description": null,
        "error": null,
        "hide": 2,
        "includeAll": false,
        "label": null,
        "multi": false,
        "name": "ALLDC",
        "options": [
          {
            "selected": true,
            "text": "HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA",
            "value": "HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA"
          }
        ],
        "query": "HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA",
        "skipUrlSync": false,
        "type": "custom"
      },
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": "AMER",
          "value": "[IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL]"
        },
        "description": null,
        "error": null,
        "hide": 0,
        "includeAll": true,
        "label": "Region",
        "multi": false,
        "name": "Region",
        "options": [
          {
            "selected": false,
            "text": "All",
            "value": "$__all"
          },
          {
            "selected": true,
            "text": "AMER",
            "value": "[IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL]"
          },
          {
            "selected": false,
            "text": "APAC",
            "value": "[HND|SYD|UKB]"
          },
          {
            "selected": false,
            "text": "EMEA",
            "value": "[CDG|LO2|LO3|FRA]"
          },
          {
            "selected": false,
            "text": "HYPERFORCE",
            "value": "HYPERFORCE"
          },
          {
            "selected": false,
            "text": "SANDBOX",
            "value": "[HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA]"
          }
        ],
        "query": "AMER : [IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL], APAC : [HND|SYD|UKB], EMEA : [CDG|LO2|LO3|FRA], HYPERFORCE , SANDBOX : [HND|SYD|UKB|IA2|IA4|IA5|AID|ORD|DFW|PH2|PHX|YHU|YUL|CDG|LO2|LO3|FRA]",
        "queryValue": "",
        "skipUrlSync": false,
        "type": "custom"
      },
      {
        "description": null,
        "error": null,
        "hide": 2,
        "label": null,
        "name": "EXCLUDELISTSB",
        "query": "(cs46,|cs995,|cs999,|cs1,|cs80,|cs49,|cs23,|cs26,|cs9,|cs18,|cs87,)",
        "skipUrlSync": false,
        "type": "constant"
      },
      {
        "description": null,
        "error": null,
        "hide": 2,
        "label": null,
        "name": "EXCLUDELISTHF",
        "query": "(.*s,|aus15,)",
        "skipUrlSync": false,
        "type": "constant"
      },
      {
        "description": null,
        "error": null,
        "hide": 2,
        "label": null,
        "name": "EXCLUDELIST",
        "query": "(cs|gs0,|gs1,|ap0,|um7,)",
        "skipUrlSync": false,
        "type": "constant"
      },
      {
        "description": null,
        "error": null,
        "hide": 2,
        "label": null,
        "name": "EXCLUDELISTHFSB",
        "query": "(usa14s,|usa6s,|usa4s,)",
        "skipUrlSync": false,
        "type": "constant"
      },
      {
        "allValue": null,
        "current": {
          "selected": false,
          "text": "aus1|aus11|aus13|aus23|aus25|aus27|aus3|aus43|aus47|aus5|aus7|aus75|aus77|aus9|bra1|bra3|can1|can11|can17|can25|can26|can27|can28|can29|deu1|deu3|deu5|fra1|fra32|fra5|fra7|ind1|ind11|ind13|ind15|ind17|ind19|ind21|ind23|ind25|ind27|ind37|ind5|ind7|ind9|jpn1|jpn17|jpn19|jpn21|jpn3|jpn5|jpn7|sgp1|sgp3|usa1|usa12|usa13|usa26|usa7",
          "value": "aus1|aus11|aus13|aus23|aus25|aus27|aus3|aus43|aus47|aus5|aus7|aus75|aus77|aus9|bra1|bra3|can1|can11|can17|can25|can26|can27|can28|can29|deu1|deu3|deu5|fra1|fra32|fra5|fra7|ind1|ind11|ind13|ind15|ind17|ind19|ind21|ind23|ind25|ind27|ind37|ind5|ind7|ind9|jpn1|jpn17|jpn19|jpn21|jpn3|jpn5|jpn7|sgp1|sgp3|usa1|usa12|usa13|usa26|usa7"
        },
        "description": null,
        "error": null,
        "hide": 2,
        "includeAll": false,
        "label": null,
        "multi": false,
        "name": "falconcells",
        "options": [
          {
            "selected": true,
            "text": "aus1|aus11|aus13|aus23|aus25|aus27|aus3|aus43|aus47|aus5|aus7|aus75|aus77|aus9|bra1|bra3|can1|can11|can17|can25|can26|can27|can28|can29|deu1|deu3|deu5|fra1|fra32|fra5|fra7|ind1|ind11|ind13|ind15|ind17|ind19|ind21|ind23|ind25|ind27|ind37|ind5|ind7|ind9|jpn1|jpn17|jpn19|jpn21|jpn3|jpn5|jpn7|sgp1|sgp3|usa1|usa12|usa13|usa26|usa7",
            "value": "aus1|aus11|aus13|aus23|aus25|aus27|aus3|aus43|aus47|aus5|aus7|aus75|aus77|aus9|bra1|bra3|can1|can11|can17|can25|can26|can27|can28|can29|deu1|deu3|deu5|fra1|fra32|fra5|fra7|ind1|ind11|ind13|ind15|ind17|ind19|ind21|ind23|ind25|ind27|ind37|ind5|ind7|ind9|jpn1|jpn17|jpn19|jpn21|jpn3|jpn5|jpn7|sgp1|sgp3|usa1|usa12|usa13|usa26|usa7"
          }
        ],
        "query": "aus1|aus11|aus13|aus23|aus25|aus27|aus3|aus43|aus47|aus5|aus7|aus75|aus77|aus9|bra1|bra3|can1|can11|can17|can25|can26|can27|can28|can29|deu1|deu3|deu5|fra1|fra32|fra5|fra7|ind1|ind11|ind13|ind15|ind17|ind19|ind21|ind23|ind25|ind27|ind37|ind5|ind7|ind9|jpn1|jpn17|jpn19|jpn21|jpn3|jpn5|jpn7|sgp1|sgp3|usa1|usa12|usa13|usa26|usa7",
        "skipUrlSync": false,
        "type": "custom"
      }
    ]
  },
  "time": {
    "from": "now-2d",
    "to": "now-5m"
  },
  "timepicker": {
    "nowDelay": "5m",
    "refresh_intervals": [
      "1m",
      "2m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ]
  },
  "timezone": "utc",
  "title": "CUJ - Service Cloud - DC, POD PRE_PROD",
  "uid": "72O_0DQ7z",
  "version": 210
}