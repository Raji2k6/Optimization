import shutil
import os

# Check if model exists
if os.path.exists('model/energy_predictor.h5'):
    # Backup the model
    shutil.copy('model/energy_predictor.h5', 'model/energy_predictor_v1_backup.h5')
    print("✅ Model backed up as: model/energy_predictor_v1_backup.h5")
else:
    print("⚠️ No existing model found to backup")

# Also backup encoders if they exist
if os.path.exists('model/scaler.pkl'):
    shutil.copy('model/scaler.pkl', 'model/scaler_v1_backup.pkl')
    print("✅ Scaler backed up")
    
if os.path.exists('model/month_encoder.pkl'):
    shutil.copy('model/month_encoder.pkl', 'model/month_encoder_v1_backup.pkl')
    print("✅ Encoder backed up")

print("\n🎉 Backup complete! Safe to retrain now.")