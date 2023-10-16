#include "nurex/nurex.h"

using namespace nurex;
int main(){
    Nucleus carbon(12,6,make_density<DensityHO>(1.548415436,1.6038565),make_density<DensityHO>(1.548415436,1.6038565));
    Nucleus ni(64,28,make_density<DensityFermi>(4.2413494,0.50732378),make_density<DensityFermi>(4.2413494,0.50732378));

    double s=0;
    for(int i=0;i<1000;++i){    
        //auto gm = make_glauber_model<MOL4C_FMD,FermiMotionD<NNCrossSectionFit>>(ni, carbon);
        auto gm = make_glauber_model<MOL>(ni, carbon);
        gm.SetRange(0.39,0.39);
        s=gm.SigmaR(100+i);
        printf("%d %lf\n\r",i,s);
    }

    return 0;
}