# :chart_with_upwards_trend: Mixed Oil Distillation (MOD)

MOD is an application that creates a new distillation profile given 2 existing crude oil profiles via the [Crude Monitor](https://www.crudemonitor.ca/) website.

### Tools used:

- Python (v3.7.7)
- Jupyter Notebook
- Pandas
- Numpy
- Matplotlib
- Selenium

  _For more info please see [requirements.txt](requirement.txt)_

### How to run the application:

1. Ensure that all cells in the Juptyer Notebook client has ran through once and that all modules have imported correctly. Failure to do so may result in an error.
2. Go on https://www.crudemonitor.ca/home.php and select the oil profile you wish to evaluate. Then click into their distillation button to view the distillation dashboard. _Note that condensate oils do not have distillation profiles_.
3. Copy the link of the distillation webpage and save it into `url_a` variable in the application cell. Do the same for another oil profile except for `url_b`.
4. Insert desired percentage volume you wish to evaluate and save it into the `percentage` variable. _Ensure the temp is between 5-99, or errors will occur_.
5. Execute the application cell and view your results.
