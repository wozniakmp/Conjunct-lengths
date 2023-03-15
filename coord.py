#function calculating syntactic complexity
def complexity(tree):
    return (len(list(tree.subtrees())) + len(tree.leaves()) - 1) / (len(tree.leaves()))

def get_parent(tree, t):
    return t[tree.treeposition()[:-1]]

def set_leaves(tree, color):
    
    leaves = tree.treepositions('leaves')
    
    for i, leaf in enumerate(leaves):
        lab = tree[leaf[:-1]].label()
        if not (lab[0] == "-" and lab[-1] == "-"):
            tree[leaves[i]] = "\\textcolor{" + color + "}{" + tree[leaves[i]]
            break
            
    for i,leaf in enumerate(leaves[::-1]):
        lab = tree[leaf[:-1]].label()
        if not (lab[0] == "-" and lab[-1] == "-"):
            tree[leaves[len(leaves)-i-1]] = tree[leaves[len(leaves)-i-1]] + "}"
            break

#function finding the governor of a coordination
def get_head(tree, t, coord_pos):

    head_dict = {'V': [['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'], ['MD'], ['TO']],
                 'P': [['IN', 'TO'], ['VBG'], ['NP', 'NP-ADV']],
                 'ADJP': [['JJ', 'JJR', 'JJS']],
                 'ADVP': [['ADV', 'RB', 'RBR', 'RBS']],
                 'S': [['TO', 'IN', 'WH'], ['VP']]
                 }
    
    n_list = ['NP', 'NN', 'NNS', 'NNP', 'NNPS', 'NML', 'NAC', 'NX']
    
    head = []
    
    label = tree.label()
    
    if label:
        if label[0] == 'N':
            if len(tree) > coord_pos + 1:
                p_head = tree[coord_pos+1]
                if p_head.label() in n_list and tree[coord_pos].label()[0] in ['N', 'U', 'A', 'Q', 'P']:
                    head.append((p_head.label(), p_head.leaves(), p_head.treeposition()))
                    
            if coord_pos > 0 and coord_pos != 100:
                p_head = tree[coord_pos-1]
                if p_head.label() in n_list and tree[coord_pos].label()[0] in ['N', 'U', 'A', 'Q', 'P', 'V']:
                    head.append((p_head.label(), p_head.leaves(), p_head.treeposition()))
                    
            if coord_pos > 1 and coord_pos != 100:
                p_head = tree[coord_pos-2]
                if tree[coord_pos-1].label() in [":", ",", ";", "“"] and p_head.label() in n_list and tree[coord_pos].label()[0] in ['N', 'U', 'A', 'Q', 'P', 'V']:
                    head.append((p_head.label(), p_head.leaves(), p_head.treeposition()))
                    
            if len(tree) > coord_pos + 2:
                p_head = tree[coord_pos+2]
                if p_head.label() in n_list and tree[coord_pos].label()[0] in ['N', 'U', 'A', 'Q', 'P', 'V'] and tree[coord_pos+1].label() in ["JJ", "NP", "PP"]:
                    head.append((p_head.label(), p_head.leaves(), p_head.treeposition()))
                    
        else:
            if label[0] == 'S':
                for group in head_dict['S']:
                    for child in tree:
                        if child.label()[:2] in group and child.treeposition()[-1] != coord_pos:
                            head.append((child.label(), child.leaves(), child.treeposition()))
            else:
                if label[0] in head_dict.keys():
                    for group in head_dict[label[0]]:
                        for child in tree:
                            if child.label() in group and child.treeposition()[-1] != coord_pos:
                                head.append((child.label(), child.leaves(), child.treeposition()))
                else:
                    if label[:4] in head_dict.keys():
                        for group in head_dict[label[:4]]:
                            for child in tree:
                                if child.label() in group and child.treeposition()[-1] != coord_pos:
                                    head.append((child.label(), child.leaves(), child.treeposition()))
    
    if head == [] and tree.label() != '':
            head = get_head(get_parent(tree, t), t, 100)
    
    return head


#function transforming a tree into a sentence which can be written in LaTeX file
def latex_sentence(tree):
    leaves = tree.leaves()
    pos = tree.treepositions('leaves')
    sen = ""
    punct = [",", ".", ";", ":", "...", "'s", "n't", "'re", "''", ")", "'"]
    slash = ["$", "%", "&", "#"]
    
    for i, leaf in enumerate(leaves):
        lab = tree[pos[i][:-1]].label()
        if lab[0] == "-" and lab[-1] == "-" and lab != "-LRB-" and lab != "-RRB-":
            continue
        if lab == "-LRB-":
            leaf = "("
        if lab == "-RRB-":
            leaf = ")"
        if leaf in punct:
            sen += leaf
        else:
            if leaf == "%":
                sen += "\\%"
            else:
                word = ""
                for char in leaf:
                    if char in slash:
                        word += "\\"
                    word += char
                if sen != "":
                    if sen[-1] == "`" or sen[-1] == "(":
                        sen = sen + word
                    else:
                        sen = sen + " " + word
                else:
                    sen = word
            
    return(sen)

#function transforming a tree into a sentence
def sentence(tree):
    leaves = tree.leaves()
    pos = tree.treepositions('leaves')
    sen = ""
    punct = [",", ".", ";", ":", "...", "'s", "n't", "'re", "''", "'", ")", "%"]
    for i, leaf in enumerate(leaves):
        lab = tree[pos[i][:-1]].label()
        if lab[0] == "-" and lab[-1] == "-" and lab != "-LRB-" and lab != "-RRB-":
            continue
        if lab == "-LRB-":
            leaf = "("
        if lab == "-RRB-":
            leaf = ")"
        if leaf in punct:
            sen += leaf
        else:
            if sen != "":
                if sen[-1] == "`" or sen[-1] == "(":
                    sen = sen + leaf
                else:
                    sen = sen + " " + leaf
            else:
                sen = leaf
            
    return(sen)

