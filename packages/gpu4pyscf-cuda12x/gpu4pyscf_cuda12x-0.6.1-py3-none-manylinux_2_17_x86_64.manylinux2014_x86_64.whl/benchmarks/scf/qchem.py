import os
import csv
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Run SCF, grad with Q-Chem for molecules')
parser.add_argument('--basis',       type=str, default='def2-tzvpp')
parser.add_argument('--xc',          type=str, default='B3LYP')
parser.add_argument('--input_path',  type=str, default='./')
parser.add_argument('--output_path', type=str, default='./')
args = parser.parse_args()
bas = args.basis
xc = args.xc

if not os.path.exists(args.output_path):
    os.mkdir(args.output_path)

os.environ['QCSCRATCH'] = '/tmp/'

def run_dft(filename):
    with open(filename, 'r') as xyz_file:
        coords = xyz_file.readlines()[2:]

    with open('qchem_input.in', "w") as input:
        input.write("$molecule\n")
        input.write("0 1\n")
        for line in coords:
            input.write(line)
        input.write("\n$end")
        input.write("\n")

        input.write("$rem\n")
        input.write("JOBTYPE force\n")
        input.write("MEM_STATIC 10000\n")
        input.write("METHOD " + args.xc + "\n")
        input.write("BASIS " + args.basis + "\n")
        input.write("SYMMETRY      FALSE\n")
        input.write("SYM_IGNORE    TRUE\n")
        input.write("XC_GRID       000099000590\n")
        input.write("NL_GRID       000050000194\n")
        input.write("MAX_SCF_CYCLES 100\n")
        input.write("SCF_CONVERGENCE 9\n")
        input.write("THRESH        14\n")
        input.write("INCDFT_DENDIFF_THRESH    14\n")
        input.write("INCDFT_GRIDDIFF_THRESH   14\n")
        input.write("BASIS_LIN_DEP_THRESH 12\n")
        input.write("$end\n")
    
    import tempfile 
    temp = tempfile.NamedTemporaryFile() 
    filename = temp.name

    import os 
    print(f'creating a temp file named {filename}')
    os.system('qchem -nt 32 qchem_input.in > ' + filename)
    
    with open(filename, 'r') as output_file:
        lines = output_file.readlines()
        for line in lines:
            if line[:16] == " SCF time:   CPU":
                info = line[16:].split(' ')[4]
                scf_time = float(info[:-1])
            if line[:20] == " Gradient time:  CPU":
                info = line[20:].split(' ')[5]
                gradient_time = float(info)
            energy_line = ' Total energy in the final basis set ='
            if energy_line in line:
                info = line.replace(energy_line, '')
                e_tot = float(info)
    return scf_time, gradient_time, e_tot

fields = ['mol', 't_scf', 't_gradient', 'e_tot']
output_file = 'qchem-32-cores-cpu.csv'
output_file = args.output_path + output_file
csvfile = open(output_file, 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)

for filename in os.listdir(args.input_path):
    if filename.endswith(".xyz"):
        print(f'running DFT {filename}')
        try:
            info = run_dft(args.input_path+filename)
            row = [filename[:-4]]+list(info)
            csvwriter.writerow(row)
            csvfile.flush()
        except:
            continue
csvfile.close()
