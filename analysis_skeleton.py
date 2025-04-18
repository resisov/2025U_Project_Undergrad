import uproot
import numpy as np
import awkward as ak
import matplotlib.pyplot as plt
import mplhep as hep

def isTightElectron(pt, eta):
    mask = ((pt > 10) & (np.abs(eta) < 1.4442)) | ((pt > 10) & (np.abs(eta) > 1.566) & (np.abs(eta) < 2.1))
    return mask
def isTightMuon(pt, eta):
    mask = (pt > 10) & (np.abs(eta) < 2.4)
    return mask
def isGoodJet(pt, eta):
    mask = (pt > 30) & (np.abs(eta) < 2.4)
    return mask

fname = "./tag_1_delphes_events.root"

# Open the ROOT file
with uproot.open(fname) as file:
    # Access the tree
    tree = file["Delphes"]
    
    # Define Electron and Muon variables
    prompt_electron_pt = tree["Electron.PT"].array()
    prompt_electron_eta = tree["Electron.Eta"].array()
    electron_mask = isTightElectron(prompt_electron_pt, prompt_electron_eta)
    electron_pt, electron_eta = prompt_electron_pt[electron_mask], prompt_electron_eta[electron_mask]

    prompt_muon_pt = tree["Muon.PT"].array()
    prompt_muon_eta = tree["Muon.Eta"].array()
    muon_mask = isTightMuon(prompt_muon_pt, prompt_muon_eta)
    muon_pt, muon_eta = prompt_muon_pt[muon_mask], prompt_muon_eta[muon_mask]

    # Define Jet variables
    prompt_jet_pt = tree["Jet.PT"].array()
    prompt_jet_eta = tree["Jet.Eta"].array()
    jet_mask = isGoodJet(prompt_jet_pt, prompt_jet_eta)
    jet_pt, jet_eta = prompt_jet_pt[jet_mask], prompt_jet_eta[jet_mask]

    # Define MET variables
    met_pt = tree["MissingET.MET"].array()
    met_phi = tree["MissingET.Phi"].array()

    # Number of Lepton should be equal to 1
    n_lepton = ak.num(electron_pt) + ak.num(muon_pt)
    electron_pt_temp = ak.firsts(electron_pt)
    muon_pt_temp = ak.firsts(muon_pt)
    # None to 0
    electron_pt_temp = ak.fill_none(electron_pt_temp, 0)
    muon_pt_temp = ak.fill_none(muon_pt_temp, 0)

    # Number of Jet should be equal or greater than 2
    n_jet = ak.num(jet_pt)

    print(((electron_pt_temp > 35) | (muon_pt_temp > 30)))
    lepton_kinematic_mask = (
        (n_lepton == 1) &
        ((electron_pt_temp > 35) | (muon_pt_temp > 30)) &
        (n_jet >= 2)
    )
    met_pt = met_pt[lepton_kinematic_mask]
    Leading_jet = ak.firsts(jet_pt[lepton_kinematic_mask])
    print(len(met_pt))

    # Plotting
    plt.style.use(hep.style.CMS)
    plt.figure(figsize=(8, 8))
    plt.hist(met_pt, bins=10, range=(0, 1000), histtype='step', color='blue',linewidth=2.5, label='Test Sample')
    plt.legend()
    plt.xlabel(r"$E_{T}^{miss}$ (GeV)")
    plt.ylabel("Events")
    plt.savefig("met_pt.png")

    plt.figure(figsize=(8, 8))
    plt.hist(Leading_jet, bins=10, range=(0, 1000), histtype='step', color='blue',linewidth=2.5, label='Test Sample')
    plt.legend()
    plt.xlabel(r"$Leading Jet PT$ (GeV)")
    plt.ylabel("Events")
    plt.savefig("Leading_jet.png")
