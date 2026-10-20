"""Plot generated aggregate observations; no fitted trends or causal labels."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'reports/annual-audit.json').read_text())['annual_audits']
years=[int(r['reporting_year']) for r in rows]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,6.2),gridspec_kw={'width_ratios':[1.15,1]})
fig.subplots_adjust(left=.07,right=.97,top=.73,bottom=.23,wspace=.28)
fig.suptitle('Cornwall-on-Hudson water accounts, 2019–2025',x=.07,y=.96,ha='left',fontsize=18,fontweight='bold',color='#16324a')
fig.text(.07,.875,'A public-report comparability audit',fontsize=12,color='#3b5366')
fig.text(.07,.825,'Calendar-day billing is an explicit assumption; billing coverage and measurement boundaries are unconfirmed.',fontsize=10,color='#46535e')
ax=axes[0]
ax.plot(years,[float(r['produced_gal'])/1e6 for r in rows],color='#206a9a',marker='o',label='Reported annual production')
ax.plot(years,[r['derived_annual_billed_gal']/1e6 for r in rows],color='#b96b32',marker='s',linestyle='--',label='Inferred annual billed volume')
ax.set_ylabel('Million US gallons');ax.set_ylim(0,330);ax.set_title('Reported production and conditional billing',loc='left',fontsize=11,pad=14)
ax.legend(loc='lower left',frameon=False,fontsize=9)
ax=axes[1]
ax.plot(years,[float(r['reported_unaccounted_pct']) for r in rows],color='#206a9a',marker='o',label='Reported unaccounted percentage')
ax.plot(years,[r['derived_unaccounted_pct'] for r in rows],color='#b96b32',marker='x',linestyle='--',label='Calendar-day implied percentage')
for y,dx,dy in [(2020,-.65,4),(2022,.15,4)]:
 row=rows[years.index(y)]
 ax.annotate(f'{y}: arithmetic differs',xy=(y,float(row['reported_unaccounted_pct'])),xytext=(y+dx,float(row['reported_unaccounted_pct'])+dy),fontsize=8,color='#7d4520',arrowprops={'arrowstyle':'-','color':'#b96b32'})
ax.set_ylim(0,48);ax.yaxis.set_major_formatter(PercentFormatter(xmax=100));ax.set_title('Reported and conditional residual shares',loc='left',fontsize=11,pad=14)
ax.legend(loc='upper right',frameon=False,fontsize=8)
for ax in axes:
 ax.set_xticks(years);ax.tick_params(axis='x',labelsize=9);ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
fig.text(.07,.13,'Inferred billing = reported daily billed × 365/366 days; it is not an observed annual ledger total.',fontsize=10,color='#46535e')
fig.text(.07,.086,'Sources: seven official annual reports; exact PDF hashes and physical pages in data/seed/annual-water.csv.',fontsize=9,color='#596672')
fig.text(.07,.044,'AI text/visual inspection completed; independent human and departmental review pending. Residual is not a leakage estimate.',fontsize=9,color='#596672')
for extension in ['png','svg']:
    output=ROOT/f'reports/annual-water-accounts.{extension}'
    fig.savefig(output,dpi=180,facecolor='white',metadata={'Description':'Conditional public-source audit; billing coverage remains unconfirmed.'})
    if extension == 'svg':
        output.write_text('\n'.join(line.rstrip() for line in output.read_text().splitlines())+'\n')
print('Generated reports/annual-water-accounts.png and .svg')
