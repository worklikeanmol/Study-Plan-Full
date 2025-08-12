# New Score-Oriented Plan Output Sample

This document shows the expected JSON output structure for new_score_oriented study plans.

## JSON Structure

```json
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-06-08",
    "target_score": "210/300",
    "total_months": 10,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 80,
    "weekend_sessions": 80,
    "dpp_sessions": 396,
    "Full_month_revision": 4
  },
  "monthly_breakdown": {
    "Month 1": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 80.75,
      "user_target_score": 56.52,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_9",
            "Chapter_8"
          ],
          "subject_weightage": 27.51,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_8",
            "Chapter_1"
          ],
          "subject_weightage": 26.46,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_2",
            "Chapter_1"
          ],
          "subject_weightage": 26.78,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 2": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 51.24,
      "user_target_score": 35.87,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 11.15,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_4",
            "Chapter_9"
          ],
          "subject_weightage": 17.91,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_8",
            "Chapter_6"
          ],
          "subject_weightage": 22.18,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 3": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 30.37,
      "user_target_score": 21.26,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_6",
            "Chapter_1"
          ],
          "subject_weightage": 3.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_11",
            "Chapter_6"
          ],
          "subject_weightage": 8.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 18.75,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 4": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 48.5,
      "user_target_score": 33.95,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_5",
            "Chapter_12"
          ],
          "subject_weightage": 25.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_2",
            "Chapter_5"
          ],
          "subject_weightage": 9.55,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_9",
            "Chapter_5"
          ],
          "subject_weightage": 13.69,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 5": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 29.62,
      "user_target_score": 20.73,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 6.81,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_12",
            "Chapter_3"
          ],
          "subject_weightage": 14.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_12",
            "Chapter_3"
          ],
          "subject_weightage": 8.45,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 58.2,
      "user_target_score": 40.74,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_10",
            "Chapter_2"
          ],
          "subject_weightage": 26.0,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_7",
            "Chapter_10"
          ],
          "subject_weightage": 23.34,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_7",
            "Chapter_10"
          ],
          "subject_weightage": 8.86,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
      "Total_PYQs_in_this_Month": 40
    },
    "Month 8": {
      "Total_PYQs_in_this_Month": 40
    },
    "Month 9": {
      "Total_PYQs_in_this_Month": 50
    },
    "Month 10": {
      "Total_PYQs_in_this_Month": 60
    }
  },
  "chapter_breakdown": {
    "month_1": {
      "mathematics": [
        "Chapter_2",
        "Chapter_1"
      ],
      "physics": [
        "Chapter_9",
        "Chapter_8"
      ],
      "chemistry": [
        "Chapter_8",
        "Chapter_1"
      ]
    },
    "month_2": {
      "mathematics": [
        "Chapter_8",
        "Chapter_6"
      ],
      "physics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "chemistry": [
        "Chapter_4",
        "Chapter_9"
      ]
    },
    "month_3": {
      "mathematics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "physics": [
        "Chapter_6",
        "Chapter_1"
      ],
      "chemistry": [
        "Chapter_11",
        "Chapter_6"
      ]
    },
    "month_4": {
      "mathematics": [
        "Chapter_9",
        "Chapter_5"
      ],
      "physics": [
        "Chapter_5",
        "Chapter_12"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_5"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_12",
        "Chapter_3"
      ],
      "physics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_12",
        "Chapter_3"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_7",
        "Chapter_10"
      ],
      "physics": [
        "Chapter_10",
        "Chapter_2"
      ],
      "chemistry": [
        "Chapter_7",
        "Chapter_10"
      ]
    }
  },
  "weekly_breakdown": {
    "month_1": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_2": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      }
    },
    "month_3": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      }
    },
    "month_4": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      }
    },
    "month_5": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_6": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

2025-08-12 11:18:16,999 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor executing
2025-08-12 11:18:16,999 - app.new_score_oriented_graph - INFO - No feedback detected, finalizing plan
=== NEW SCORE ORIENTED PLAN DEBUG ===
Plan keys: ['user_id', 'target_score', 'exam_date', 'total_months', 'syllabus_completion_months', 'practice_months', 'monthly_plans', 'revision_flow_results', 'overall_strategy', 'dependency_analysis', 'coverage_validation', 'target_achievement_probability', 'enhanced_features', 'calendar_plan', 'monthly_targets_data', 'extended_months_plan', 'weekend_schedule', 'weekly_topic_breakdown', 'user_target_score', 'start_date', 'end_date', 'overall_summary']
Plan type: <class 'dict'>
Plan content preview: {'user_id': 'user_xytmcw7wk', 'target_score': 210, 'exam_date': '2026-06-12', 'total_months': 10, 'syllabus_completion_months': 6, 'practice_months': 4, 'monthly_plans': [], 'revision_flow_results': {'physics': {'chapters': [{'chapter': 'Chapter_9', 'weightage': 14.77, 'category': 'High', 'coverage_percentage': 1.0, 'priority_reason': 'dependency_optimized', 'dependencies_satisfied': True, 'completion_order': 1, 'dependency_level': 0, 'dependencies': [], 'coverage_reason': 'complete_syllabus_cov...
=====================================
=== STUDY PLAN RESPONSE DEBUG ===
Response keys: ['insights', 'monthly_plan', 'weekly_plan', 'new_score_oriented_data']
Monthly plan keys: ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']
====================================

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-06-08 | Target: 210/300

10
Months
132
Study Days
80
PYQ Days
80
Weekend Sessions
396
DPP Sessions

📊 MONTHLY TARGET BREAKDOWN:
--------------------------------------------------

Month 1
70.0% of target
80.8
Total Achievable Score
56.5
Your Target Score
Efficiency Required
70.0%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_9', 'Chapter_8'], 'subject_weightage': 27.51, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_8', 'Chapter_1'], 'subject_weightage': 26.46, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_2', 'Chapter_1'], 'subject_weightage': 26.78, 'chapter_count': 2}

Month 2
70.0% of target
51.2
Total Achievable Score
35.9
Your Target Score
Efficiency Required
70.0%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 11.15, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_4', 'Chapter_9'], 'subject_weightage': 17.91, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_8', 'Chapter_6'], 'subject_weightage': 22.18, 'chapter_count': 2}

Month 3
70.0% of target
30.4
Total Achievable Score
21.3
Your Target Score
Efficiency Required
70.0%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_6', 'Chapter_1'], 'subject_weightage': 3.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_11', 'Chapter_6'], 'subject_weightage': 8.36, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 18.75, 'chapter_count': 2}

Month 4
70.0% of target
48.5
Total Achievable Score
34.0
Your Target Score
Efficiency Required
70.0%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_5', 'Chapter_12'], 'subject_weightage': 25.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_5'], 'subject_weightage': 9.55, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_5'], 'subject_weightage': 13.69, 'chapter_count': 2}

Month 5
70.0% of target
29.6
Total Achievable Score
20.7
Your Target Score
Efficiency Required
70.0%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 6.81, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_12', 'Chapter_3'], 'subject_weightage': 14.36, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_12', 'Chapter_3'], 'subject_weightage': 8.45, 'chapter_count': 2}

Month 6
70.0% of target
58.2
Total Achievable Score
40.7
Your Target Score
Efficiency Required
70.0%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_2'], 'subject_weightage': 26.0, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_7', 'Chapter_10'], 'subject_weightage': 23.34, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_7', 'Chapter_10'], 'subject_weightage': 8.86, 'chapter_count': 2}

Weekly Breakdown
--------------------------------------------------

--- Month 1 Weekly Breakdown ---

mathematics
Chapter_2
  Topic_2
  Topic_4
  Topic_6
  Topic_7
  Topic_8
  Topic_10
  Topic_11
  Topic_1
  Topic_3
  Topic_5
  Topic_9
11 topics
Chapter_1
  Topic_6
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_5
  Topic_7
7 topics

physics
Chapter_9
  Topic_1
  Topic_3
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_7
  Topic_8
8 topics
Chapter_8
  Topic_1
  Topic_10
  Topic_11
  Topic_12
  Topic_13
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_8
  Topic_9
13 topics

chemistry
Chapter_8
  Topic_1
  Topic_5
  Topic_7
  Topic_8
  Topic_9
  Topic_10
  Topic_6
  Topic_11
  Topic_12
  Topic_2
  Topic_3
  Topic_4
  Topic_13
13 topics
Chapter_1
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
  Topic_7
7 topics

--- Month 2 Weekly Breakdown ---

mathematics
Chapter_8
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_11
  Topic_12
  Topic_13
  Topic_9
  Topic_1
  Topic_3
  Topic_6
  Topic_10
13 topics
Chapter_6
  Topic_2
  Topic_3
  Topic_4
  Topic_1
4 topics

physics
Chapter_11
  Topic_2
  Topic_5
  Topic_7
  Topic_1
  Topic_6
  Topic_3
  Topic_4
7 topics
Chapter_4
  Topic_1
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_3
6 topics

chemistry
Chapter_4
  Topic_2
  Topic_3
  Topic_5
  Topic_4
  Topic_6
  Topic_1
6 topics
Chapter_9
  Topic_8
  Topic_1
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
8 topics

--- Month 3 Weekly Breakdown ---

mathematics
Chapter_11
  Topic_7
  Topic_1
  Topic_6
  Topic_2
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_4
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
6 topics

physics
Chapter_6
  Topic_1
  Topic_2
  Topic_3
  Topic_4
4 topics
Chapter_1
  Topic_2
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_7
  Topic_4
7 topics

chemistry
Chapter_11
  Topic_6
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_6
  Topic_1
  Topic_4
  Topic_2
  Topic_3
4 topics

--- Month 4 Weekly Breakdown ---

mathematics
Chapter_9
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_7
  Topic_5
  Topic_6
  Topic_8
8 topics
Chapter_5
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
7 topics

physics
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics
Chapter_12
  Topic_1
  Topic_2
  Topic_4
  Topic_7
  Topic_12
  Topic_3
  Topic_5
  Topic_6
  Topic_10
  Topic_11
  Topic_8
  Topic_9
12 topics

chemistry
Chapter_2
  Topic_1
  Topic_2
  Topic_5
  Topic_7
  Topic_9
  Topic_11
  Topic_3
  Topic_6
  Topic_10
  Topic_4
  Topic_8
11 topics
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics

--- Month 5 Weekly Breakdown ---

mathematics
Chapter_12
  Topic_1
  Topic_3
  Topic_11
  Topic_2
  Topic_6
  Topic_7
  Topic_8
  Topic_12
  Topic_4
  Topic_5
  Topic_9
  Topic_10
12 topics
Chapter_3
  Topic_8
  Topic_1
  Topic_2
  Topic_6
  Topic_3
  Topic_4
  Topic_5
  Topic_7
8 topics

physics
Chapter_3
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_7
  Topic_8
8 topics
Chapter_7
  Topic_1
  Topic_3
  Topic_5
  Topic_8
  Topic_10
  Topic_2
  Topic_6
  Topic_9
  Topic_4
  Topic_7
  Topic_11
11 topics

chemistry
Chapter_12
  Topic_1
  Topic_5
  Topic_7
  Topic_4
  Topic_6
  Topic_8
  Topic_9
  Topic_10
  Topic_11
  Topic_12
  Topic_2
  Topic_3
12 topics
Chapter_3
  Topic_7
  Topic_8
  Topic_3
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_6
8 topics

--- Month 6 Weekly Breakdown ---

mathematics
Chapter_7
  Topic_2
  Topic_4
  Topic_6
  Topic_10
  Topic_3
  Topic_7
  Topic_8
  Topic_9
  Topic_11
  Topic_1
  Topic_5
11 topics
Chapter_10
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_14
  Topic_15
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_13
16 topics

physics
Chapter_10
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_9
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_11
  Topic_15
  Topic_1
  Topic_13
  Topic_14
16 topics
Chapter_2
  Topic_3
  Topic_9
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_6
  Topic_10
  Topic_11
11 topics

chemistry
Chapter_7
  Topic_3
  Topic_5
  Topic_2
  Topic_4
  Topic_8
  Topic_1
  Topic_6
  Topic_7
  Topic_9
  Topic_10
  Topic_11
11 topics
Chapter_10
  Topic_2
  Topic_4
  Topic_5
  Topic_10
  Topic_13
  Topic_15
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_14
  Topic_16
  Topic_1
  Topic_3
  Topic_6
  Topic_8
16 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-06-08",
    "target_score": "210/300",
    "total_months": 10,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 80,
    "weekend_sessions": 80,
    "dpp_sessions": 396,
    "Full_month_revision": 4
  },
  "monthly_breakdown": {
    "Month 1": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 80.75,
      "user_target_score": 56.52,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_9",
            "Chapter_8"
          ],
          "subject_weightage": 27.51,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_8",
            "Chapter_1"
          ],
          "subject_weightage": 26.46,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_2",
            "Chapter_1"
          ],
          "subject_weightage": 26.78,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 2": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 51.24,
      "user_target_score": 35.87,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 11.15,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_4",
            "Chapter_9"
          ],
          "subject_weightage": 17.91,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_8",
            "Chapter_6"
          ],
          "subject_weightage": 22.18,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 3": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 30.37,
      "user_target_score": 21.26,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_6",
            "Chapter_1"
          ],
          "subject_weightage": 3.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_11",
            "Chapter_6"
          ],
          "subject_weightage": 8.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 18.75,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 4": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 48.5,
      "user_target_score": 33.95,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_5",
            "Chapter_12"
          ],
          "subject_weightage": 25.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_2",
            "Chapter_5"
          ],
          "subject_weightage": 9.55,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_9",
            "Chapter_5"
          ],
          "subject_weightage": 13.69,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 5": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 29.62,
      "user_target_score": 20.73,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 6.81,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_12",
            "Chapter_3"
          ],
          "subject_weightage": 14.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_12",
            "Chapter_3"
          ],
          "subject_weightage": 8.45,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "70.0% of target",
      "total_achievable_score": 58.2,
      "user_target_score": 40.74,
      "efficiency_required": "70.0%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_10",
            "Chapter_2"
          ],
          "subject_weightage": 26.0,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_7",
            "Chapter_10"
          ],
          "subject_weightage": 23.34,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_7",
            "Chapter_10"
          ],
          "subject_weightage": 8.86,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
      "Total_PYQs_in_this_Month": 40
    },
    "Month 8": {
      "Total_PYQs_in_this_Month": 40
    },
    "Month 9": {
      "Total_PYQs_in_this_Month": 50
    },
    "Month 10": {
      "Total_PYQs_in_this_Month": 60
    }
  },
  "chapter_breakdown": {
    "month_1": {
      "mathematics": [
        "Chapter_2",
        "Chapter_1"
      ],
      "physics": [
        "Chapter_9",
        "Chapter_8"
      ],
      "chemistry": [
        "Chapter_8",
        "Chapter_1"
      ]
    },
    "month_2": {
      "mathematics": [
        "Chapter_8",
        "Chapter_6"
      ],
      "physics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "chemistry": [
        "Chapter_4",
        "Chapter_9"
      ]
    },
    "month_3": {
      "mathematics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "physics": [
        "Chapter_6",
        "Chapter_1"
      ],
      "chemistry": [
        "Chapter_11",
        "Chapter_6"
      ]
    },
    "month_4": {
      "mathematics": [
        "Chapter_9",
        "Chapter_5"
      ],
      "physics": [
        "Chapter_5",
        "Chapter_12"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_5"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_12",
        "Chapter_3"
      ],
      "physics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_12",
        "Chapter_3"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_7",
        "Chapter_10"
      ],
      "physics": [
        "Chapter_10",
        "Chapter_2"
      ],
      "chemistry": [
        "Chapter_7",
        "Chapter_10"
      ]
    }
  },
  "weekly_breakdown": {
    "month_1": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_2": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      }
    },
    "month_3": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      }
    },
    "month_4": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          }
        }
      }
    },
    "month_5": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 19
          },
          "chemistry": {
            "chapters": {
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_6": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 27
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      }
    }
  }
}


```