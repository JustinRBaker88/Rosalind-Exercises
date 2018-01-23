    def motif_enumeration(Dna, k, d)
        Patterns <- an empty set
        for each k-mer Pattern in Dna
            for each k-mer Pattern’ differing from Pattern by at most d
              mismatches
                if Pattern' appears in each string from Dna with at most d
                mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns