import os
import glob
from itertools import chain, combinations


def sep_path_basename_ext(file_in):

    # separate path and file name
    f_path, file_name = os.path.split(file_in)
    if f_path == '':
        f_path = '.'

    # separate file basename and extension
    f_base, f_ext = os.path.splitext(file_name)

    return f_path, f_base, f_ext


def powerset(iterable):

    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"

    s = list(iterable)  # allows duplicate elements
    chain_obj = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    combo_lol = []
    for _, combo in enumerate(chain_obj, 1):
        if len(list(combo)) > 0:
            combo_lol.append(list(combo))

    return combo_lol


########################################################################################################################

# file in
ip_dir              = '/Users/songweizhi/Desktop/DateArTree/01_HGT_ALE_with_OMA'
round_list          = [1, 2, 3, 4, 5]
color_list          = ['dodgerblue', 'goldenrod1', 'darkorange1', 'seagreen3', 'orchid3']
min_detected_times  = 2

# file out
op_dir      = '/Users/songweizhi/Desktop/demo_op'

########################################################################################################################

rscript     = '%s/rscript.R' % op_dir
plot_file   = '%s/Venn.pdf'  % op_dir

if os.path.isdir(op_dir):
    os.system('rm -r %s' % op_dir)
os.system('mkdir %s' % op_dir)

########################################################################################################################

hgt_dict = dict()
rd_to_hgt_dict= dict()
for each_rd in round_list:

    rd_id               = each_rd
    current_rd_op_dir   = '%s/ALE4_op_dir_%s_0.3'   % (ip_dir, each_rd)
    pdf_file_re         = '%s/*.%s'                 % (current_rd_op_dir, 'pdf')
    pdf_file_list       = glob.glob(pdf_file_re)

    rd_to_hgt_dict[rd_id] = set()

    for each_pdf in pdf_file_list:
        f_path, f_base, f_ext = sep_path_basename_ext(each_pdf)
        f_base_split = f_base.split('_')
        id_by_d_to_r = '%s_to_%s'   % (f_base_split[3], f_base_split[5])
        rd_og        = '%s_%s'    % (each_rd, f_base_split[0])
        rd_og_value  = '%s_%s_%s' % (each_rd, f_base_split[0], f_base_split[6])

        rd_to_hgt_dict[rd_id].add(id_by_d_to_r)

        if id_by_d_to_r not in hgt_dict:
            hgt_dict[id_by_d_to_r] = []
        hgt_dict[id_by_d_to_r].append(rd_og_value)

################################################### get Venn diagram ###################################################

combination_list = powerset(round_list)

value_str_list = []
for each_cmbo in combination_list:
    current_str = ''
    if len(each_cmbo) == 1:
        current_value = rd_to_hgt_dict[each_cmbo[0]]
        current_str = 'area%s=%s' % (each_cmbo[0], len(current_value))
        value_str_list.append(current_str)
    else:
        value_lol = []
        for each_element in each_cmbo:
            ele_value = rd_to_hgt_dict[each_element]
            value_lol.append(ele_value)
        shared = set(value_lol[0]).intersection(*value_lol)
        current_str = 'n%s=%s' % (''.join([str(i) for i in each_cmbo]), len(shared))
        value_str_list.append(current_str)

value_str     = ', '.join(value_str_list)
label_str     = '"' + '", "'.join([str(i) for i in round_list]) + '"'
color_str     = '"' + '", "'.join([str(i) for i in color_list]) + '"'
font_size_str = ', '.join(['1.2']*len(combination_list))

rscript_handle = open(rscript, 'w')
rscript_handle.write('library(futile.logger)\n')
rscript_handle.write('library(gridBase)\n')
rscript_handle.write('library(VennDiagram)\n')
rscript_handle.write('pdf(file="%s")\n' % plot_file)
rscript_handle.write('venn.plot <- draw.quintuple.venn(%s, category=c(%s), fill=c(%s), cat.col=c(%s), cat.cex=1.2, cat.dist=0.3, margin=0.05, cex=c(%s), ind=TRUE)\n' % (value_str, label_str, color_str, color_str, font_size_str))
rscript_handle.write('dev.off()\n')
rscript_handle.close()

os.system('Rscript %s' % rscript)

########################################################################################################################

qualified_hgt_num = 0
for each_hgt in hgt_dict:
    occurence_list = hgt_dict[each_hgt]
    pdf_dir = '%s/%s_%s' % (op_dir, each_hgt, len(occurence_list))
    if len(occurence_list) >= min_detected_times:
        print('%s\t%s' % (each_hgt, occurence_list))
        qualified_hgt_num += 1
        os.system('mkdir %s' % pdf_dir)
        for each_h in occurence_list:
            rd_id               = each_h.split('_')[0]
            og_id               = each_h.split('_')[1]
            value               = each_h.split('_')[2]
            pwd_input_pdf_in    = '%s/ALE4_op_dir_%s_0.3/%s_HGT_*_%s_%s.pdf'  % (ip_dir, rd_id, og_id, each_hgt,value)
            pwd_input_pdf_out   = '%s/%s_%s_%s_%s.pdf'                        % (pdf_dir, rd_id, og_id, each_hgt,value)
            os.system('cp %s %s' % (pwd_input_pdf_in, pwd_input_pdf_out))

print('The number of HGTs detected in >= %s runs is %s.' % (min_detected_times, qualified_hgt_num))
print('Done!')
