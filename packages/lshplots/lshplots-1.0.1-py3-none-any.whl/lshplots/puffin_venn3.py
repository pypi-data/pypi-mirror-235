
def puffin_venn3(subsets, func='sqrt', **kwargs):
    """
    Plots a 3-set venn diagram with subset sizes proportional to the square/cube root of the subset size.
    Useful when the subset sizes are very different.
    subsets are assumed to be in the order: Abc, aBc, ABc, abC, AbC, aBC, ABC
                                            100, 010, 110, 001, 101, 011, 111

    The subsets parameter can be one of the following:
     - A list (or a tuple), containing three set objects.
     - A list (or a tuple) with 7 numbers, denoting the sizes of the regions in the following order:
        [Abc, aBc, ABc, abC, AbC, aBC, ABC]
        [100, 010, 110, 001, 101, 011, 111].
    """

    from matplotlib_venn import venn3, venn3_circles
    from matplotlib_venn._venn3 import compute_venn3_subsets

    ### check inputs
    if len(subsets) == 3:
        subsets = compute_venn3_subsets(*subsets)

    if len(subsets) != 7:
        raise ValueError("Expected 7 subset sizes, got %d" % len(subsets))
    
    if np.any(np.array(subsets) < 0):
        raise ValueError("Expected subset sizes to be non-negative")
    
    if 'set_colors' not in kwargs:
        kwargs['set_colors'] = ('#5FB4D5', '#ED3F43', '#F89C30')
        set_intersect_color = True
        
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 1

    if func == 'sqrt':
        new_subsets = np.sqrt(subsets)
    elif func == 'cbrt':
        new_subsets = np.cbrt(subsets)
    else:
        raise ValueError("Expected 'sqrt' or 'cbrt' for func, got %s" % func)
    
    ### plot venn diagram
    v = venn3(new_subsets, **kwargs)

    ### set subset labels
    locs = ['100', '010', '110', '001', '101', '011', '111']
    for i in range(7):
        try:
            v.get_label_by_id(locs[i]).set_text(subsets[i])
        except:
            pass
    
    ### set patch colors
    patch_list = ['011','101', '110', '111']
    patch_colors = ['gainsboro', 'gainsboro', 'gainsboro', 'silver']
    if set_intersect_color == True:
        try:
            for i in range(4):
                v.get_patch_by_id(patch_list[i]).set_color(patch_colors[i])

        except:
            pass

    ### draw circles
    venn3_circles(new_subsets, linestyle='solid', linewidth=1.5, color='dimgray')


    return v # not sure if returning v is correct