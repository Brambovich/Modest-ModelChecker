# TODO:
# - read schedule info from modest (somehow)
# - verify it with KiBaM
# - make a nice graph out of it

import pandas as pd 
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# from matplotlib import gridspec
# from matplotlib.gridspec import GridSpec
from pandas import date_range, to_datetime
from numpy import logical_or, logical_and, arange, amax, zeros, array, pad, subtract, logical_not
# import uppaal # should be removed later on

# pgf_with_custom_preamble = {
#         "font.size": 30,
#         "text.usetex": True,    # use inline math for ticks
#         "pgf.rcfonts": False,   # don't setup fonts from rc parameters
#         "pgf.preamble": [
#              r"\usepackage[utf8x]{inputenc}",
#              r"\usepackage[T1]{fontenc}",
#             ]
# }
# mpl.rcParams.update(pgf_with_custom_preamble)
# mpl.use('Agg')
# plt.style.use('bmh')
# mpl.rcParams['lines.linewidth'] = 3

def createBatteryCSV(output):
    
    # Manual values to generate a test schedule
    # output.loc[4:, 'load'] = -2000
    # output.loc[30:, 'load'] = 5000
    # output.loc[95:, 'load'] = 2346
    # output.loc[140:, 'load'] = -2464
    # output.loc[183:, 'load'] = 9235
    # output.loc[256:, 'load'] = 2847
    # output.loc[301:, 'load'] = -1243
    # output.loc[333:, 'load'] = -50
    # output.loc[451:, 'load'] = 3413
    # output.loc[490:, 'load'] = 12000
    # output.loc[501:, 'load'] = 2459
    # output.loc[540:, 'load'] = -6000
    # output.loc[598:, 'load'] = -3000
    # output.loc[603:, 'load'] = 2395
    # output.loc[611:, 'load'] = 1245
    # output.loc[678:, 'load'] = 4394
    # output.loc[705:, 'load'] = -4000
    # output.loc[779:, 'load'] = -3593
    # output.loc[800:, 'load'] = 3143
    # output.loc[808:, 'load'] = 1934
    # output.loc[834:, 'load'] = 9823
    # output.loc[894:, 'load'] = -3023
    # output.loc[911:, 'load'] = -2452
    # output.loc[954:, 'load'] = 5000

    # initialize battery dataframe
    battery = pd.DataFrame(data={'gc' : [0,0], 'soc' : [0,0]})
    print(battery)

    # counter for battery dataframe rows
    j = 2

    for i in range(1, output.shape[0]):
        output.loc[i, 'gc'] = 60*output.loc[i, 'gc']
        # print(output.loc[i])
        
        if output.loc[i, 'soc'] != output.loc[i - 1, 'soc']:
            # if j == 2:
            #     prevtime = int(0)
            # else: 
            prevtime = battery.loc[j-1, 'gc']
            load = int((output.loc[i, 'soc'] - output.loc[i - 1, 'soc']) / (output.loc[i, 'gc'] - prevtime)) 
            row = output.loc[i,['gc','soc']]
            battery.loc[j - 1, 'soc'] = load
            battery = battery.append(row, ignore_index=True)
            battery.loc[j, 'soc'] = load
            j += 2 # skip two as two rows are added
            battery = battery.append(row, ignore_index=True)
            #print(battery,"\n")

    battery = battery.rename(columns={'soc' : 'load'})
    battery = battery.loc[:battery.shape[0] - 2,:] # delete last row
    print(battery)
    battery.to_csv('battery.csv', index=False)

# def savefig(fig, fname):
#     fig.patch.set_facecolor('black')
#     fig.patch.set_alpha(0)
#     fig.savefig(fname,bbox_inches='tight',
#         facecolor=fig.get_facecolor()
#         )

# def plotWindows(ax, df, i):
#     sun = 'Scheduled' not in df
#     ax.hlines(
#         (0 if sun else i) + zeros(df.shape[0]),
#         unix(df['Start Time (UTCG)']),
#         unix(df['Stop Time (UTCG)']),
#         color = 'orange' if sun else array(['silver','black'])[df['Scheduled']],
#         alpha = 0.7,
#         lw = 25
#     )
#     return ax

# def plotSchedule(data):
#     # ================================================
#     print('Plotting schedule ...\n')
#     # ================================================

#     f = plt.figure(figsize=[25,12])
#     gs = gridspec.GridSpec(2, 1, height_ratios=[4,2],hspace=0.1)

#     xticks     = date_range(to_datetime('20/03/2016 07:00:00'), to_datetime('21/03/2016 07:00:00'), freq = '1h')
#     xticks    = xticks[1:] # for layout reasons remove first tick

#     # SoC_filtered,_ = tools.filter(trace[['gc','soc']], 'soc', which='first' )

#     ax = plt.subplot(gs[0])
#     # soc = uppaal.plotSoC( # plotting SoC curve of Uppaal
#     #     ax = ax,
#     #     data = SoC_filtered,
#     #     xticks = xticks
#     # )

#     # ax = plt.subplot(gs[1])
#     # load = uppaal.plotLoad( # plotting Load curve of Uppaal
#     #     ax = ax,
#     #     data = load_filtered,
#     #     xticks = xticks
#     # )

#     ax1 = ax.twinx()
#     i = 1
#     yticklabels = []

#     ax1.grid(False)
#     for df in data.values(): # plotting timewindows
#         plotWindows(ax1, df, i)
#     #     yticklabels.insert(
#     #         0 if df['id'] == 'Sun' else i,
#     #         '$\\mathit{' + df['id'] + '}$'
#     #     )
#     #     i += 0 if df['id'] == 'Sun' else 1

#     ax1.set(
#         xlim = [to_datetime('20/03/2016 07:00:00'), to_datetime('21/03/2016 07:00:00')], # some hardcoded timestamps for now
#         ylim = [-0.5,len(data)-0.5],
#         yticks = arange(0,len(data)),
#         yticklabels = yticklabels
#     )

#     s, = plt.plot([],[],'silver',lw=25)
#     s2, = plt.plot([],[],'black',lw=25)
#     #sun, = plt.plot([],[],'orange',lw=20)

#     f.legend(
#         (s2, s),
#         ('scheduled','skipped'),
#         loc = "upper center",
#         labelspacing = 0.04,
#         ncol = 4
#     )

#     f.autofmt_xdate()
#     savefig(f,'schedule.pdf')

# 'Main'
fname = "out.csv"
output = pd.read_csv(fname)
createBatteryCSV(output)
# plotSchedule(output)