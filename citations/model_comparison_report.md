================================================================================
LLM MODEL COMPARISON REPORT
================================================================================

## Models Tested

  dartmouth_anthropic.claude-haiku-4-5-20251001_short dartmouth    anthropic.claude-haiku-4-5-20251001 short  47 classifications
  dartmouth_google.gemma-3-27b-it_full               dartmouth    google.gemma-3-27b-it full   81 classifications
  dartmouth_google.gemma-3-27b-it_short              dartmouth    google.gemma-3-27b-it short  47 classifications
  dartmouth_openai.gpt-oss-120b_full                 dartmouth    openai.gpt-oss-120b  full   81 classifications
  dartmouth_openai.gpt-oss-120b_short                dartmouth    openai.gpt-oss-120b  short  47 classifications

## Classification Comparison Matrix

### Relationship Type Distributions

**dartmouth_anthropic.claude-haiku-4-5-20251001_short** (47 classifications):
  CitesAsDataSource               20 ( 42.6%)
  Uses                            12 ( 25.5%)
  IsDocumentedBy                  10 ( 21.3%)
  CitesForInformation              3 (  6.4%)
  Compiles                         2 (  4.3%)

**dartmouth_google.gemma-3-27b-it_full** (81 classifications):
  Uses                            53 ( 65.4%)
  IsDocumentedBy                  20 ( 24.7%)
  CitesAsDataSource                5 (  6.2%)
  Cites                            3 (  3.7%)

**dartmouth_google.gemma-3-27b-it_short** (47 classifications):
  CitesAsDataSource               25 ( 53.2%)
  IsDocumentedBy                  20 ( 42.6%)
  Uses                             2 (  4.3%)

**dartmouth_openai.gpt-oss-120b_full** (81 classifications):
  Uses                            27 ( 33.3%)
  Cites                           24 ( 29.6%)
  IsDocumentedBy                  11 ( 13.6%)
  CitesAsEvidence                 10 ( 12.3%)
  CitesAsDataSource                5 (  6.2%)
  Compiles                         2 (  2.5%)
  cites                            1 (  1.2%)
  CitesForInformation              1 (  1.2%)

**dartmouth_openai.gpt-oss-120b_short** (47 classifications):
  Uses                            28 ( 59.6%)
  IsDocumentedBy                   8 ( 17.0%)
  CitesAsDataSource                4 (  8.5%)
  Compiles                         3 (  6.4%)
  CitesAsEvidence                  2 (  4.3%)
  Cites                            1 (  2.1%)
  CitesForInformation              1 (  2.1%)

## Model Agreement Analysis

### Pairwise Agreement Rates

Models are sorted by agreement rate.

  dartmouth_google.gemma-3-27b-it_full     <-> dartmouth_openai.gpt-oss-120b_short     : 53.2% (25/47)
  dartmouth_openai.gpt-oss-120b_full       <-> dartmouth_openai.gpt-oss-120b_short     : 51.1% (24/47)
  dartmouth_google.gemma-3-27b-it_full     <-> dartmouth_google.gemma-3-27b-it_short   : 48.9% (23/47)
  dartmouth_google.gemma-3-27b-it_full     <-> dartmouth_openai.gpt-oss-120b_full      : 43.2% (35/81)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short <-> dartmouth_google.gemma-3-27b-it_full    : 42.6% (20/47)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short <-> dartmouth_google.gemma-3-27b-it_short   : 40.4% (19/47)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short <-> dartmouth_openai.gpt-oss-120b_short     : 38.3% (18/47)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short <-> dartmouth_openai.gpt-oss-120b_full      : 36.2% (17/47)
  dartmouth_google.gemma-3-27b-it_short    <-> dartmouth_openai.gpt-oss-120b_short     : 27.7% (13/47)
  dartmouth_google.gemma-3-27b-it_short    <-> dartmouth_openai.gpt-oss-120b_full      : 19.1% (9/47)

## Short Context vs Full Text Comparison

**dartmouth_google.gemma-3-27b-it**:
  Common citations: 47
  Agreement: 48.9% (23/47)
  Sample disagreements:
    dandi.000690         short=CitesAsDataSource    full=Uses                
    dandi.000692         short=CitesAsDataSource    full=Uses                
    dandi.000472         short=CitesAsDataSource    full=Uses                
    dandi.000053         short=CitesAsDataSource    full=Uses                
    dandi.001359         short=CitesAsDataSource    full=Uses                

**dartmouth_openai.gpt-oss-120b**:
  Common citations: 47
  Agreement: 51.1% (24/47)
  Sample disagreements:
    dandi.001195         short=Uses                 full=Cites               
    dandi.000472         short=Compiles             full=Uses                
    dandi.000053         short=CitesAsDataSource    full=Cites               
    dandi.001354         short=Uses                 full=Cites               
    dandi.000563         short=Uses                 full=Cites               

## Confidence Score Analysis

  dartmouth_anthropic.claude-haiku-4-5-20251001_short avg=0.82 min=0.72 max=0.95
  dartmouth_google.gemma-3-27b-it_full               avg=0.92 min=0.50 max=0.95
  dartmouth_google.gemma-3-27b-it_short              avg=0.84 min=0.75 max=0.95
  dartmouth_openai.gpt-oss-120b_full                 avg=0.60 min=0.00 max=0.96
  dartmouth_openai.gpt-oss-120b_short                avg=0.78 min=0.00 max=0.95

## Citations with Low Model Agreement

Citations with most disagreement:

**dandi.001349** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.78)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.001354** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.66)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.000563** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.78)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.000690** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.75)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.001195** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.78)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.001359** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.75)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.001366** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.78)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.001375** (DOI: 10.1038/s41597-025-06285-x...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.78)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    IsDocumentedBy       (0.95)
  dartmouth_google.gemma-3-27b-it_full     IsDocumentedBy       (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesAsDataSource    (0.75)

**dandi.001174** (DOI: 10.1101/2025.07.17.663965...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.73)
  dartmouth_openai.gpt-oss-120b_full       CitesAsEvidence      (0.86)
  dartmouth_google.gemma-3-27b-it_short    CitesAsDataSource    (0.75)
  dartmouth_google.gemma-3-27b-it_full     Uses                 (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesForInformation  (0.72)

**dandi.001375** (DOI: 10.1101/2025.07.17.663965...)
  dartmouth_openai.gpt-oss-120b_short      Uses                 (0.78)
  dartmouth_openai.gpt-oss-120b_full       Cites                (0.00)
  dartmouth_google.gemma-3-27b-it_short    CitesAsDataSource    (0.75)
  dartmouth_google.gemma-3-27b-it_full     Uses                 (0.95)
  dartmouth_anthropic.claude-haiku-4-5-20251001_short CitesForInformation  (0.75)
