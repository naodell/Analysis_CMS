#ifndef _TCPHYSOBJECT_H
#define	_TCPHYSOBJECT_H


#include "TObject.h"
#include "TLorentzVector.h"
#include "TVector2.h"
#include "TVector3.h"
#include <map>
#include <utility>
#include <string>
#include <iostream>

using namespace std;

class TCPhysObject : public TLorentzVector {
    private:
        TVector3 _vtx;
        map<string, float> _IdMap;
        int  _charge;
        bool _isPF;
        bool _isTriggered;
        bool _isFake;
        string _type;

    public:
        TCPhysObject();
        TCPhysObject(TLorentzVector p4, int charge);
        TCPhysObject(TLorentzVector p4, int charge, string type);
        virtual ~TCPhysObject();

        // "get" methods -----------

        float IdMap(string key) const;
        TVector2 P2() const;
        TVector3 Vtx() const;
        int Charge() const;  
        string Type() const;
        bool IsPF() const;
        bool IsFake() const;
        bool IsTriggered() const;

        float Dxy(TVector3 *primVtx) const;
        float Dz(TVector3 *primVtx) const;

        // "set" methods ---------
        void SetP4(TLorentzVector p4);
        void SetIdMap(string s, float v);
        //void SetIsoMap(string s, float v);
        void SetVtx(float vx, float vy, float vz);
        void SetCharge(int c);  
        void SetType(string);
        void SetPF(bool);
        void SetTriggered(bool);
        void SetFake(bool);

        // print method
        virtual ostream& TCprint(ostream& out) const;

        ClassDef(TCPhysObject, 2);
};

inline ostream& operator<<(ostream& os, const TCPhysObject& ph){ 
  return ph.TCprint(os);
}

#endif	/* _TCPHYSOBJECT_H */
